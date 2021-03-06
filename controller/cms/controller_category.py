from flask import request
from service.cms.service_category import sCategory


class cCategory:
    def c_category():
        try:
            json = request.get_json()
            sCategory.s_create_category(json)
            return {"msg": "Categoria criada.", "status": 201}, 201
        except Exception as err:
            if err.errno == 1062:
                return {"msg": "Categoria já existe.", "status": 409}, 409
            print("cms -> c_category ->", err)
            return {"msg": "Falha nossa.", "status": 500}, 500
