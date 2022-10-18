from models.database import execut_query
from models import model_color


def s_create_color(json):
    execut_query().insert(model_color.q_insert_color, json)
    return True
