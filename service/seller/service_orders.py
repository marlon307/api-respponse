from models.database import MySQLCnn
from models import model_orders


def list_orders_seller(json):
    execut_query = MySQLCnn()
    list = execut_query.select(model_orders.q_order_seller, json)
    execut_query.finishExecution

    return list
