from flask import request
from service.cms.service_size import sSize


class cSize:
    def c_size():
        try:
            json = request.get_json()
            sSize.s_create_size(json)
            return {"msg": "Tamanho criado.", "status": 201}, 201
        except Exception as err:
            if err.errno == 1062:
                return {"msg": "Este tamnho já existe.", "status": 409}, 409
            print("cms -> c_size ->", err)
            return {"msg": "Falha nossa.", "status": 500}, 500
