from models.database import MySQLCnn
from models import model_orders
import json


def get_orders(data_json):
    execut_query = MySQLCnn()
    orders = execut_query.select(model_orders.q_get_orders, data_json)
    execut_query.finishExecution()
    return orders


def get_orderid(data_json):
    execut_query = MySQLCnn()
    order = execut_query.selectOne(model_orders.q_get_order_id, data_json)
    execut_query.finishExecution()
    if {} != order:
        order["address"] = json.loads(order["address"])
        order["carrier"] = json.loads(order["carrier"])
        order["list_products"] = json.loads(order["list_products"])
        return order
    return False
