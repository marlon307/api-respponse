from models.database import execut_query
from models import mode_gender


def s_create_gender(json):
    execut_query(mode_gender.q_insert_gender).insert(json)
    return True
