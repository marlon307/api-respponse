from models.database import MySQLCnn
from models import model_bag
from utility.process_payment import process_payment_card, process_payment_pix


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


def list_bag(user_id):
    execut_query = MySQLCnn()
    list_bag = execut_query.select(model_bag.q_list_bag, {"user_id": user_id})
    execut_query.finishExecution()

    if list_bag != {}:

        return {
            "list_b": list_bag,
        }
    return False


def register_order(data_json, task):
    json_for_tuple = (
        data_json["p_userid"],
        data_json["address"],
        data_json["carrie"],
        data_json["method_pay"],
        data_json["shipping"],
    )
    execut_query = MySQLCnn()
    order = execut_query.callProcedure("register_order", json_for_tuple)
    execut_query.finishExecution()

    new_dict = dict()
    if data_json["method_pay"] == "pix" and "number_order" in order[0]:
        payment = process_payment_pix(data_json["method_pay"], order[0])
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

    elif "number_order" in order[0]:
        task.add_task(
            process_payment_card, data_json["method_pay"], {**order[0], **data_json}
        )
        new_dict = {
            "number_order": order[0]["number_order"],
        }
        return new_dict
    return False
