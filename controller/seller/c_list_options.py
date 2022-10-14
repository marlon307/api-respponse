from flask import request
from service.seller.service_list_options_prod import sSeller


class cOptions:
    def c_options():
        try:
            list_options = sSeller.s_list_option()
            return {
                "detail": "Lista de opções.",
                "list": list_options,
                "status": 200,
            }, 200
        except Exception as err:
            print("seller -> c_list_options_seller_register_product ->", err)
            return {"detail": "Falha nossa.", "status": 500}, 500
