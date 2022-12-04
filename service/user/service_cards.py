from models.database import execut_query
from models import model_cards


def s_add_cards(json):
    execut_query(model_cards.q_insert_card).insert(json)
    return True
