from flask import request
from service.user.service_order import sOrders

msgErr500 = {"msg": "Server error.", "status": 500}, 500


class cOrders:
    def c_get_order_id(id):
        try:

            json = {
                "user_id": request.headers["user"]["id_user"],
                "order_id": int(id),
            }
            order = sOrders.s_get_orderid(json)
            return {
                "msg": "Pedido listado.",
                "status": 200,
                "order": order,
            }, 200
        except Exception as err:
            print("bag -> c_get_order ->", err)
            return {"msg": "Falha nossa.", "status": 500}, 500
