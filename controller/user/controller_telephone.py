from flask import request
from service.user.service_telephone import sTelephone


class cTelephone:
    def c_add_telephone():
        try:
            json = request.get_json()
            json["user_id"] = request.headers["user"]["id_user"]
            sTelephone.s_add_telephone(json)

            return {"msg": "Telefone adicionado.", "status": 201}, 201
        except Exception as err:
            print("telephone -> c_add_telephone ->", err)
            return {"msg": "Falha nossa.", "status": 500}, 500
