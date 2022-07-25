from datetime import datetime, timedelta
from flask import request, jsonify
from service.user.service_address import sAddress


class cAddress:
    def c_add_address():
        try:
            json = request.get_json()
            sAddress.s_add_address(json)

            return {"msg": "Endereço adicionado.", "status": 201}, 201
        except Exception as err:
            print("address -> c_add_address ->", err)
            return {"msg": "Falha nossa.", "status": 500}, 500
