from models.database import execut_query
from models.mode_gender import qGender


class sGender:
    def s_create_gender(json):
        execut_query().insert(qGender.q_insert_gender(), json)
        return True
