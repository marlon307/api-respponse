from models.database import execut_query
from models.model_orders import qOrder
import json


class sOrders:
    def s_get_orders(data_json):
        orders = execut_query.select(qOrder.q_get_orders(), data_json)
        return orders

    def s_get_orderid(data_json):
        order = execut_query.selectOne(qOrder.q_get_order_id(), data_json)
        order["address"] = json.loads(order["address"])
        order["carrier"] = json.loads(order["carrier"])
        order["list_products"] = json.loads(order["list_products"])
        return order
