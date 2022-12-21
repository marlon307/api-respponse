import json
import os
import requests
from models.database import MySQLCnn
from models import model_bag


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
        model_bag.q_get_producs_carrier, {"user_id": data["user_id"]}
    )
    execut_query.finishExecution()

    url = os.getenv("MELHORENVIO_API") + "api/v2/me/shipment/calculate"
    payload = json.dumps(
        {
            "from": {"postal_code": os.getenv("MELHORENVIO_ZIPCODE")},
            "to": {"postal_code": data["zipcode"]},
            "products": list_products,
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


def list_bag(user_id):
    execut_query = MySQLCnn()
    list_bag = execut_query.select(model_bag.q_list_bag, {"user_id": user_id})
    execut_query.finishExecution()

    if list_bag != {}:

        return {
            "list_b": list_bag,
        }
    return False


def register_order(data_json):
    json_for_tuple = (
        data_json["p_userid"],
        data_json["address"],
        data_json["carrie"],
        16.65,
    )
    execut_query = MySQLCnn()
    order = execut_query.callProcedure("register_order", json_for_tuple)
    execut_query.finishExecution()
    return order[0]
