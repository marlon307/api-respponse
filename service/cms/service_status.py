from models.database import execut_query
from models.model_status import qStatus


class sStatus:
    def s_create_status(json):
        execut_query.insert(qStatus.q_insert_status(), json)
        return True
