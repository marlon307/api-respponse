from models.database import MySQLCnn
from models import model_category


def s_create_category(json):
    execut_query = MySQLCnn
    execut_query.insert(model_category.q_insert_category, json)
    execut_query.finishExecution

    return True
