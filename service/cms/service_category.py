from models.database import execut_query
from models import model_category


def s_create_category(json):
    execut_query(model_category.q_insert_category).insert(json)
    return True
