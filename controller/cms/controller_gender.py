from service.cms.service_gender import sGender


class cGender:
    def c_gender(json):
        try:
            sGender.s_create_gender(json)
            return {"detail": "Género criado.", "status": 201}
        except Exception as err:
            if err.errno == 1062:
                return {"detail": "Género já existe.", "status": 409}
            print("cms -> c_category ->", err)
            return {"detail": "Falha nossa.", "status": 500}
