from models.database import MySQLCnn
from models import model_cards


def s_add_cards(json):
    execut_query = MySQLCnn()
    execut_query.insert(model_cards.q_insert_card, json)
    execut_query.finishExecution
    return True
