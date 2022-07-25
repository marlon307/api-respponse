from models.database import execut_query
from models.model_telephone import qTelephone


class sTelephone:
    def s_add_telephone(json):
        def format_json(value):
            return {"user_id": json["user_id"], **value}

        new_json = map(format_json, json["n_phones"])

        execut_query.insertMany(qTelephone.q_insert_telephone(), new_json)
        return True
