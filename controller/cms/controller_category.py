from service.cms.service_category import sCategory


class cCategory:
    def c_category(json):
        try:
            sCategory.s_create_category(json)
            return {"detail": "Categoria criada.", "status": 201}
        except Exception as err:
            if err.errno == 1062:
                return {"detail": "Categoria já existe.", "status": 409}
            print("cms -> c_category ->", err)
            return {"detail": "Falha nossa.", "status": 500}
