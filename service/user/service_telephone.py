from models.database import execut_query
from models.model_telephone import qTelephone


class sTelephone:
    def s_add_telephone(json):
        execut_query.insert(qTelephone.q_insert_telephone(), json)
        return True
