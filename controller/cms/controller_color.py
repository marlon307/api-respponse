from flask import request
from service.cms.service_color import sColor


class cColor:
    def c_color():
        try:
            json = request.get_json()
            sColor.s_create_color(json)
            return {"msg": "Cor criada.", "status": 201}, 201
        except Exception as err:
            if err.errno == 1062:
                return {"msg": "Esta cor já existe.", "status": 409}, 409
            print("cms -> c_color ->", err)
            return {"msg": "Falha nossa.", "status": 500}, 500
