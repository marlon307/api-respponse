from service.cms.service_size import sSize


class cSize:
    def c_size(json):
        try:
            sSize.s_create_size(json)
            return {"detail": "Tamanho criado.", "status": 201}
        except Exception as err:
            if err.errno == 1062:
                return {"detail": "Este tamnho já existe.", "status": 409}
            print("cms -> c_size ->", err)
            return {"detail": "Falha nossa.", "status": 500}
