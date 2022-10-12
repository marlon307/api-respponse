from flask import request
from service.user.service_order import sOrders

msgErr500 = {"detail": "Server error.", "status": 500}, 500


class cOrders:
    def c_get_orders():
        try:
            json = {"user_id": request.headers["user"]["id_user"]}
            orders = sOrders.s_get_orders(json)
            return {
                "detail": "Lista de pedidos.",
                "status": 200,
                "orders": orders,
            }, 200
        except Exception as err:
            print("bag -> c_get_list_orders ->", err)
            return {"detail": "Falha nossa.", "status": 500}, 500

    def c_get_order_id(id):
        try:
            json = {
                "user_id": request.headers["user"]["id_user"],
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
            return {"detail": "Falha nossa.", "status": 500}, 500
