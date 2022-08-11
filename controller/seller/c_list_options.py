from flask import request
from service.seller.service_list_options_prod import sSeller


class cOptions:
    def c_options():
        try:
            list_options = sSeller.s_list_option()
            return {"msg": "Lista de opções.", "list": list_options, "status": 200}, 200
        except Exception as err:
            if err.errno == 1062:
                return {"msg": "Este tamnho já existe.", "status": 409}, 409
            print("seller -> c_list_options_seller_register_product ->", err)
            return {"msg": "Falha nossa.", "status": 500}, 500
