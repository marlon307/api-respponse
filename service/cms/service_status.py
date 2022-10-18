from models.database import execut_query
from models import model_status


def s_create_status(json):
    execut_query(model_status.q_insert_status).insert(json)
    return True
