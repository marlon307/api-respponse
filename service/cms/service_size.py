from models.database import MySQLCnn
from models import mode_size


def s_create_size(json):
    execut_query = MySQLCnn()
    execut_query.insert(mode_size.q_insert_size, json)
    execut_query.finishExecution

    return True
