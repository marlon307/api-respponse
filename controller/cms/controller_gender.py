from flask import request
from service.cms.service_gender import sGender


class cGender:
    def c_gender():
        try:
            json = request.get_json()
            sGender.s_create_gender(json)
            return {"detail": "Género criado.", "status": 201}, 201
        except Exception as err:
            if err.errno == 1062:
                return {"detail": "Género já existe.", "status": 409}, 409
            print("cms -> c_category ->", err)
            return {"detail": "Falha nossa.", "status": 500}, 500
