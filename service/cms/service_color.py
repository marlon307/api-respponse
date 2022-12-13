from models.database import execut_query
from models import model_color


def s_create_color(json):
    execut_query(model_color.q_insert_color).insert(json)
    execut_query.finishExecution

    return True
