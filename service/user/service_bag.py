import json
import os
import requests
from models.database import MySQLCnn
from models import model_bag, model_carrier
from utility.process_payment import process_payment


def add_bag(data):
    execut_query = MySQLCnn()
    existBag = execut_query.selectOne(model_bag.q_check_prod_bag, data)

    if "sizes_id" in existBag:
        data["quantity"] = existBag["quantity"] + 1
        execut_query.update(model_bag.q_bag_update_quantity, data)
    else:
        execut_query.insert(model_bag.q_insert_bag, data)

    execut_query.finishExecution()
    return True


def update_quantity_bag(data):
    execut_query = MySQLCnn()
    execut_query.update(model_bag.q_bag_update_quantity, data)
    execut_query.finishExecution()
    return True


def s_delete_item_bag(data):
    execut_query = MySQLCnn()
    execut_query.delete(model_bag.q_bag_delete_item, data)
    execut_query.finishExecution()
    return True


def s_calc_shipping(data):
    execut_query = MySQLCnn()
    list_products = execut_query.select(
        model_bag.q_get_producs_carrier,
        {
            "user_id": data["user_id"],
            "id_order": data["order_id"] if "order_id" in data else None,
        },
    )
    execut_query.finishExecution()

    url = os.getenv("MELHORENVIO_API") + "api/v2/me/shipment/calculate"
    payload = json.dumps(
        {
            "from": {"postal_code": os.getenv("MELHORENVIO_ZIPCODE")},
            "to": {"postal_code": data["zipcode"]},
            "products": list_products,
            "services": str(data["services"]) if "services" in data else "",
        }
    )
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer %s" % (os.getenv("MELHORENVIO_TOKEN")),
        "User-Agent": os.getenv("MELHORENVIO_EMAIL_SUPORTE"),
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    data = response.json()

    if type(data) is list:
        new_list = list()
        for carrier in data:
            if "error" not in carrier:
                new_list.append(
                    {
                        "id": carrier["id"],
                        "name_carrier": carrier["company"]["name"],
                        "toDate": carrier["custom_delivery_time"],
                        "price": float(carrier["price"]),
                    }
                )
        return new_list
    return data


def list_bag(user_id):
    execut_query = MySQLCnn()
    list_bag = execut_query.select(model_bag.q_list_bag, {"user_id": user_id})
    execut_query.finishExecution()

    if list_bag != {}:

        return {
            "list_b": list_bag,
        }
    return False


def recalc_carrier(data, order):
    new_data = {
        "services": data["carrie"],
        "user_id": data["p_userid"],
        "zipcode": order["zipcode"],
        "order_id": order["number_order"],
    }
    value_shipping = s_calc_shipping(new_data)

    execut_query = MySQLCnn()
    execut_query.update(
        model_carrier.q_update_value_shipping,
        {
            "order_id": order["number_order"],
            "delivery_value": float(value_shipping["price"]),
            "p_userid": data["p_userid"],
        },
    )
    execut_query.finishExecution()


def register_order(data_json):
    json_for_tuple = (
        data_json["p_userid"],
        data_json["address"],
        data_json["carrie"],
        data_json["method_pay"],
    )
    execut_query = MySQLCnn()
    order = execut_query.callProcedure("register_order", json_for_tuple)
    execut_query.finishExecution()
    payment = process_payment(data_json["method_pay"], order[0])

    new_dict = {
        "number_order": order[0]["number_order"],
        "zipcode": order[0]["zipcode"],
        "date_of_expiration": payment["date_of_expiration"].replace(" ", ""),
        "qr_code": payment["point_of_interaction"]["transaction_data"]["qr_code"],
        "transaction_amount": payment["transaction_amount"],
        "qr_code_base64": payment["point_of_interaction"]["transaction_data"][
            "qr_code_base64"
        ],
    }

    return new_dict
