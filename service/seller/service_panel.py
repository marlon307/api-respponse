import json
from models.database import MySQLCnn
from models import model_orders, model_seller


def service_panel_seller(json):
    execut_query = MySQLCnn()
    order_info = execut_query.select(model_orders.q_panel_order_seller, json)
    qunatity_product_seller = execut_query.selectOne(
        model_orders.q_products_seller, json
    )
    execut_query.finishExecution()

    return {
        "order": order_info,
        "products": qunatity_product_seller,
    }


def service_get_panel_seller_settings(data):
    execut_query = MySQLCnn()
    data["iduser"] = None
    data = execut_query.selectOne(model_seller.q_select_seller_settings, data)
    execut_query.finishExecution()
    data["address"] = json.loads(data["address"])
    data["boxes"] = json.loads(data["boxes"])
    return data


def service_panel_seller_settings(json):
    list_box = list()
    for box in json["listboxes"]:
        box["user_id"] = json["id_user"]
        list_box.append(box)

    list_del = list()
    for idbox in json["removeboxes"]:
        list_del.append({"user_id": json["id_user"], "idbox": idbox})

    del json["listboxes"]
    del json["removeboxes"]

    execut_query = MySQLCnn()
    execut_query.insertMany(model_seller.q_insert_boxes_seller, list_box)
    execut_query.deleteMany(model_seller.q_delete_boxes, list_del)
    execut_query.update(model_seller.q_update_settings_seller, json)
    execut_query.finishExecution()
    return True
