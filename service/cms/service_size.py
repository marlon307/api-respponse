from models.database import MySQLCnn
from models import model_size


def s_create_size(json):
    execut_query = MySQLCnn()
    execut_query.insert(model_size.q_insert_size, json)
    execut_query.finishExecution()

    return True
