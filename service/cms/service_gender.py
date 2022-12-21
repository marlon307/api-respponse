from models.database import MySQLCnn
from models import model_gender


def s_create_gender(json):
    execut_query = MySQLCnn()
    execut_query.insert(model_gender.q_insert_gender, json)
    execut_query.finishExecution()

    return True
