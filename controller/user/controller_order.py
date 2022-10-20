from service.user import service_order
from utility.handleErr import handlerErr


def get_orders(c_user):
    try:
        json = {"user_id": c_user.id_user}
        orders = service_order.s_get_orders(json)
        return {
            "detail": "Lista de pedidos.",
            "status": 200,
            "orders": orders,
        }, 200
    except Exception as err:
        raise handlerErr("bag -> c_get_list_orders -> %s" % err)


def get_order_id(id, c_user):
    try:
        json = {
            "user_id": c_user["id_user"],
            "order_id": int(id),
        }
        order = service_order.s_get_orderid(json)
        return {
            "detail": "Pedido listado.",
            "status": 200,
            "order": order,
        }, 200
    except Exception as err:
        raise handlerErr("bag -> c_get_order -> %s" % err)
