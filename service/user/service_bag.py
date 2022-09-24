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

    def s_update_quantity_bag(json):
        execut_query.update(qBag.q_bag_update_quantity(), json)
        return True

    def s_delete_item_bag(json):
        execut_query.delete(qBag.q_bag_delete_item(), json)
        return True

    def s_register_order(data_json):
        json_for_tuple = (
            data_json["p_userid"],
            data_json["address"],
            data_json["carrie"],
            16.65,
        )
        order = execut_query.callProcedure("register_order", json_for_tuple)
        return order[0]
