from flask import request
from service.user.service_cards import sCards


class cCards:
    def c_add_cards():
        try:
            json = request.get_json()
            json["user_id"] = request.headers["user"]["id_user"]
            sCards.s_add_cards(json)

            return {"msg": "Cartão adicionado.", "status": 201}, 201
        except Exception as err:
            print("cards -> c_add_card ->", err)
            return {"msg": "Falha nossa.", "status": 500}, 500
