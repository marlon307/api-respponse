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
