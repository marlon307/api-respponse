from models.database import execut_query
from models import model_bag
from utility.calca_discount import calc_discount
import json


def add_bag(json):
    id_insert = execut_query(model_bag.q_insert_bag).insert(json)
    return id_insert


def list_bag(user_id):
    list_bag = execut_query(model_bag.q_list_bag).selectOne({"user_id": user_id})
    list_bag["list_add"] = json.loads(list_bag["list_add"])
    list_bag["list_b"] = json.loads(list_bag["list_b"])

    def calc_dicount(object_calc):
        old_price = calc_discount(object_calc["discount"], object_calc["price"])
        return {
            **object_calc,
            "oldPrice": old_price,
        }

    list_bag["list_b"] = list(map(calc_dicount, list_bag["list_b"]))
    return list_bag


def update_quantity_bag(json):
    execut_query(model_bag.q_bag_update_quantity).update(json)
    return True


def s_delete_item_bag(json):
    execut_query(model_bag.q_bag_delete_item).delete(json)
    return True


def s_register_order(data_json):
    json_for_tuple = (
        data_json["p_userid"],
        data_json["address"],
        data_json["carrie"],
        16.65,
    )
    order = execut_query("register_order").callProcedure(json_for_tuple)
    return order[0]
