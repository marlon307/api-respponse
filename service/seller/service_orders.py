from models.database import execut_query
from models import model_orders


def list_orders_seller(json):
    list = execut_query(model_orders.q_order_seller).select(json)
    execut_query.finishExecution

    return list
