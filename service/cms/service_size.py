from models.database import execut_query
from models import mode_size


def s_create_size(json):
    execut_query(mode_size.q_insert_size).insert(json)
    execut_query.finishExecution

    return True
