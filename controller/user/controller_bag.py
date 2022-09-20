from flask import request
from service.user.service_bag import sBag


class cBag:
    def c_add_bag():
        try:
            json = request.get_json()
            json["user_id"] = request.headers["user"]["id_user"]
            product = sBag.s_add_bag(json)

            return {
                "msg": "Produto adicionado a sacola.",
                "item_bag": product,
                "status": 201,
            }, 201
        except Exception as err:
            print("bag -> c_add_bag ->", err)
            return {"msg": "Falha nossa.", "status": 500}, 500

    def c_list_bag():
        try:
            list_items = sBag.s_list_bag(request.headers["user"]["id_user"])
            return {
                "msg": "Lista da sacola.",
                "list_bag": list_items,
                "status": 200,
            }, 200
        except Exception as err:
            print("bag -> c_list_bag ->", err)
            return {"msg": "Falha nossa.", "status": 500}, 500

    def c_bag_update_quantity():
        try:
            json = request.get_json()
            json["user_id"] = request.headers["user"]["id_user"]
            sBag.s_update_quantity_bag(json)
            return {
                "msg": "Quantidade atualizada.",
                "status": 200,
            }, 200
        except Exception as err:
            print("bag -> c_update_bag ->", err)
            return {"msg": "Falha nossa.", "status": 500}, 500

    def c_bag_delete():
        try:
            json = request.get_json()
            json["user_id"] = request.headers["user"]["id_user"]
            sBag.s_delete_item_bag(json)
            return {
                "msg": "Produto removido da sacola.",
                "status": 200,
            }, 200
        except Exception as err:
            print("bag -> c_delete_bag ->", err)
            return {"msg": "Falha nossa.", "status": 500}, 500
