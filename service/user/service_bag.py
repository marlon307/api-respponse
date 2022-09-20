from models.database import execut_query
from models.model_bag import qBag
from utility.calca_discount import calc_discount


class sBag:
    def s_add_bag(json):
        id_insert = execut_query.insert(qBag.q_insert_bag(), json)
        return id_insert

    def s_list_bag(user_id):

        list_bag = execut_query.select(qBag.q_list_bag(), {"user_id": user_id})

        def calc_dicount(object_calc):
            old_price = calc_discount(object_calc["discount"], object_calc["price"])
            return {
                **object_calc,
                "oldPrice": old_price,
            }

        list_bag = map(calc_dicount, list_bag)
        return list(list_bag)
