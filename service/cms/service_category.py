from models.database import execut_query
from models.model_category import qCategory


def s_create_category(json):
    execut_query().insert(qCategory.q_insert_category(), json)
    return True
