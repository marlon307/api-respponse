from models.database import MySQLCnn
from models import model_orders


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
