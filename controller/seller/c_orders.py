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
        raise handlerErr("seller -> c_seller_orders -> %s" % err)


def seller_order_id(id, c_user):
    try:
        order = service_orders.id_order_seller(
            {
                "user_id": c_user.id_user,
                "order_id": id,
            }
        )
        return {
            "detail": "Pedido.",
            "order": order,
            "status": 200,
        }
    except Exception as err:
        raise handlerErr("seller -> c_seller_order_id -> %s" % err)


def seller_order_id_update_status(id, data, c_user):
    try:
        service_orders.id_order_seller_update_status(
            {"order_id": id, "status_id": data["status"]}
        )
        return {
            "detail": "Status pedido.",
            "status": 200,
        }
    except Exception as err:
        raise handlerErr("seller -> c_seller_order_id -> %s" % err)
