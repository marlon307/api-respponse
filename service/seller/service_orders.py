import json
from models.database import MySQLCnn
from models import model_orders


def list_orders_seller(json):
    execut_query = MySQLCnn()
    list = execut_query.select(model_orders.q_order_seller, json)
    execut_query.finishExecution()
    return list


def id_order_seller(data):
    execut_query = MySQLCnn()
    orderId = execut_query.selectOne(model_orders.q_get_order_id_seller, data)
    execut_query.finishExecution()

    orderId["list_products"] = json.loads(orderId["list_products"])
    orderId["carrier"] = json.loads(orderId["carrier"])
    orderId["address"] = json.loads(orderId["address"])
    return orderId
