from models.database import execut_query
from models.model_bag import qBag


class sBag:
    def s_add_bag(json):
        id_insert = execut_query.insert(qBag.q_insert_bag(), json)
        return id_insert

    def s_list_bag(user_id):
        list_bag = execut_query.select(qBag.q_list_bag(), {"user_id": user_id})
        return list_bag
