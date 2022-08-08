from flask import request
from service.user.service_address import sAddress


class cAddress:
    def c_add_address():
        try:
            json = request.get_json()
            json["user_id"] = request.headers["user"]["id_user"]
            sAddress.s_add_address(json)

            return {"msg": "Endereço adicionado.", "status": 201}, 201
        except Exception as err:
            print("address -> c_add_address ->", err)
            return {"msg": "Falha nossa.", "status": 500}, 500

    def c_get_address():
        try:
            list_address = sAddress.s_get_address(request.headers["user"]["id_user"])
            return {
                "msg": "Lista de endereço.",
                "address": list_address,
                "status": 200,
            }, 200
        except Exception as err:
            print("address -> c_get_address ->", err)
            return {"msg": "Falha nossa.", "status": 500}, 500

    def c_delete_address():
        try:
            id_user = request.headers["user"]["id_user"]
            json = request.get_json()

            sAddress.s_delete_address(id_user, json["address"])
            return {
                "msg": "Endereço excluído.",
                "status": 200,
            }, 200
        except Exception as err:
            print("address -> c_delete_address ->", err)
            return {"msg": "Falha nossa.", "status": 500}, 500
