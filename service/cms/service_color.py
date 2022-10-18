from models.database import execut_query
from models.model_color import qColor


def s_create_color(json):
    execut_query().insert(qColor.q_insert_color(), json)
    return True
