from models.database import execut_query
from models.model_orders import qOrder


class sOrders:
    def s_get_orderid(json):
        order = execut_query.selectOne(qOrder.q_get_order_id(), json)
        return order
