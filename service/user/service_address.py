from models.database import execut_query
from models.model_address import qAddress


class sAddress:
    def s_add_address(json):
        execut_query.insert(qAddress.q_insert_address(), json)
        return True
