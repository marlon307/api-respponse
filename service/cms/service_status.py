from models.database import MySQLCnn
from models import model_status


def s_create_status(json):
    execut_query = MySQLCnn()
    execut_query.insert(model_status.q_insert_status, json)
    execut_query.finishExecution
    return True
