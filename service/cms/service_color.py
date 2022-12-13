from models.database import MySQLCnn
from models import model_color


def s_create_color(json):
    execut_query = MySQLCnn()
    execut_query.insert(model_color.q_insert_color, json)
    execut_query.finishExecution
    return True
