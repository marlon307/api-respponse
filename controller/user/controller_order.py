from fastapi import status, HTTPException
from service.user.service_order import sOrders

msgErr500 = HTTPException(
    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    detail="Server error.",
)


class cOrders:
    def c_get_orders(c_user):
        try:
            json = {"user_id": c_user["id_user"]}
            orders = sOrders.s_get_orders(json)
            return {
                "detail": "Lista de pedidos.",
                "status": 200,
                "orders": orders,
            }, 200
        except Exception as err:
            print("bag -> c_get_list_orders ->", err)
            raise msgErr500

    def c_get_order_id(id, c_user):
        try:
            json = {
                "user_id": c_user["id_user"],
                "order_id": int(id),
            }
            order = sOrders.s_get_orderid(json)
            return {
                "detail": "Pedido listado.",
                "status": 200,
                "order": order,
            }, 200
        except Exception as err:
            print("bag -> c_get_order ->", err)
            raise msgErr500
