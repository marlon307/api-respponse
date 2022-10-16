from service.cms.service_status import sStatus


class cStatus:
    def c_status(json):
        try:
            sStatus.s_create_status(json)
            return {"detail": "Status criado.", "status": 201}
        except Exception as err:
            if err.errno == 1062:
                return {"detail": "Este status já existe.", "status": 409}
            print("cms -> c_size ->", err)
            return {"detail": "Falha nossa.", "status": 500}
