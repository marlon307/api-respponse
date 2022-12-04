from service.seller import service_orders
from utility.handleErr import handlerErr


def seller_orders(sts, c_user):
    try:
        list_orders = service_orders.list_orders_seller(
            {
                "status_id": sts,
                "id_user": c_user.id_user,
            }
        )
        return {
            "detail": "Lista de pedidos.",
            "orders": list_orders,
            "status": 200,
        }
    except Exception as err:
        raise handlerErr("seller -> c_list_options_seller_register_product -> %s" % err)
