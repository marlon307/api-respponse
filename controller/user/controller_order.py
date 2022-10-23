from service.user import service_order
from utility.handleErr import handlerErr, JSONResponse, status


def get_orders(c_user):
    try:
        json = {"user_id": c_user.id_user}
        orders = service_order.get_orders(json)
        return {
            "detail": "Lista de pedidos.",
            "status": 200,
            "orders": orders,
        }
    except Exception as err:
        raise handlerErr("bag -> c_get_list_orders -> %s" % err)


def get_order_id(id, c_user):
    try:
        json = {
            "user_id": c_user.id_user,
            "order_id": int(id),
        }
        order = service_order.get_orderid(json)
        if order is not False:
            return {
                "detail": "Pedido listado.",
                "status": 200,
                "order": order,
            }
        return JSONResponse(
            content={
                "detail": "Não encontramos este pedido.",
                "status": 200,
            },
            status_code=200,
        )
    except Exception as err:
        raise handlerErr("bag -> c_get_order -> %s" % err)
