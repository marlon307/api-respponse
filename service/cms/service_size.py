from models.database import execut_query
from models.mode_size import qSize


class sSize:
    def s_create_size(json):
        execut_query().insert(qSize.q_insert_size(), json)
        return True
