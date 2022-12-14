from models.database import MySQLCnn
from models import mode_gender


def s_create_gender(json):
    execut_query = MySQLCnn()
    execut_query.insert(mode_gender.q_insert_gender, json)
    execut_query.finishExecution()

    return True
