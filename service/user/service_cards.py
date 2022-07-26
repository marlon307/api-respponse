from models.database import execut_query
from models.model_cards import qCards


class sCards:
    def s_add_cards(json):
        execut_query.insert(qCards.q_insert_card(), json)
        return True
