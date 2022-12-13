from models.database import MySQLCnn
from models import model_bag


def add_bag(json):
    execut_query = MySQLCnn()
    id_insert = execut_query.insert(model_bag.q_insert_bag, json)
    execut_query.finishExecution
    return id_insert


def list_bag(user_id):
    execut_query = MySQLCnn()
    list_bag = execut_query.select(model_bag.q_list_bag, {"user_id": user_id})
    main_address = execut_query.selectOne(
        model_bag.q_main_add_bag, {"user_id": user_id}
    )
    carrier = execut_query.select(model_bag.q_carrie_bag)
    execut_query.finishExecution

    def calcCarrie(carrieOpt):
        carrieOpt["price"] = 12.0
        carrieOpt["toDate"] = 3
        return carrieOpt

    carrier = map(calcCarrie, carrier)

    if list_bag != {}:

        return {
            "list_b": list_bag,
            "main_add": main_address,
            "shipping_company": list(carrier),
        }
    return False


def update_quantity_bag(json):
    execut_query = MySQLCnn()
    execut_query.update(model_bag.q_bag_update_quantity, json)
    execut_query.finishExecution
    return True


def s_delete_item_bag(json):
    execut_query = MySQLCnn()
    execut_query.delete(model_bag.q_bag_delete_item, json)
    execut_query.finishExecution
    return True


def register_order(data_json):
    json_for_tuple = (
        data_json["p_userid"],
        data_json["address"],
        data_json["carrie"],
        16.65,
    )
    execut_query = MySQLCnn()
    order = execut_query.callProcedure("register_order", json_for_tuple)
    execut_query.finishExecution
    return order[0]
