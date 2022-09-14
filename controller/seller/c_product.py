from flask import request
from service.seller.service_product import sProduct


class cProduct:
    def c_product():
        try:
            json = request.form.getlist("body")[0]
            files = request.files

            sProduct.s_create_product(json, files)
            return {
                "msg": "Produto criado com sucesso.",
                "status": 201,
            }, 201
        except Exception as err:
            print("seller -> c_create_product ->", err)
            return {"msg": "Falha nossa.", "status": 500}, 500

    def c_list_product():
        try:

            list_product = sProduct.s_list_product()
            return {
                "list": list_product,
                "msg": "Produto listado.",
                "status": 200,
            }, 200
        except Exception as err:
            print("seller -> c_list_product ->", err)
            return {"msg": "Falha nossa.", "status": 500}, 500

    def c_get_product_id(id_product):
        try:

            product_id = sProduct.s_get_product_id(id_product)
            return {
                "product": product_id,
                "msg": "Produto listado.",
                "status": 200,
            }, 200
        except Exception as err:
            print("seller -> c_get_product_id ->", err)
            return {"msg": "Falha nossa.", "status": 500}, 500
