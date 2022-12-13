from models.database import execut_query
from models import model_orders
import json


def get_orders(data_json):
    orders = execut_query(model_orders.q_get_orders).select(data_json)
    execut_query.finishExecution
    return orders


def get_orderid(data_json):
    order = execut_query(model_orders.q_get_order_id).selectOne(data_json)
    execut_query.finishExecution
    if {} != order:
        order["address"] = json.loads(order["address"])
        order["carrier"] = json.loads(order["carrier"])
        order["list_products"] = json.loads(order["list_products"])
        return order
    return False
