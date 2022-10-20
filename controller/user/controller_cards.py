from service.user.service_cards import sCards
from utility.handleErr import handlerErr


class cCards:
    def c_add_cards():
        try:
            # json = request.get_json()
            # json["user_id"] = request.headers["user"]["id_user"]
            sCards.s_add_cards("json")

            return {"detail": "Cartão adicionado.", "status": 201}
        except Exception as err:
            raise handlerErr("cards -> c_add_card -> %s" % err)
