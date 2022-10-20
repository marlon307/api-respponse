from service.user import service_bag
from utility.handleErr import handlerErr


def c_add_bag(json, c_user):
    try:
        json["user_id"] = c_user["id_user"]
        product = service_bag.s_add_bag(json)

        return {
            "detail": "Produto adicionado a sacola.",
            "item_bag": product,
            "status": 201,
        }
    except Exception as err:
        raise handlerErr("bag -> c_add_bag -> %s" % err)


def c_list_bag(c_user):
    try:
        list_items = service_bag.s_list_bag(c_user["id_user"])
        return {
            "detail": "Lista da sacola.",
            "infobag": list_items,
            "status": 200,
        }
    except Exception as err:
        raise handlerErr("bag -> c_list_bag -> %s" % err)


def c_bag_update_quantity(json, c_user):
    try:
        json["user_id"] = c_user["id_user"]
        service_bag.s_update_quantity_bag(json)

        return {
            "detail": "Quantidade atualizada.",
            "status": 200,
        }
    except Exception as err:
        raise handlerErr("bag -> c_update_bag -> %s" % err)


def c_bag_delete(json, c_user):
    try:
        json["user_id"] = c_user["id_user"]
        service_bag.s_delete_item_bag(json)
        return {
            "detail": "Produto removido da sacola.",
            "status": 200,
        }
    except Exception as err:
        raise handlerErr("bag -> c_delete_bag -> %s" % err)


def c_bag_register_order(json, c_user):
    try:
        json["p_userid"] = c_user["id_user"]
        order = service_bag.s_register_order(json)
        return {
            "detail": "Produto removido da sacola.",
            "status": 200,
            "order": order,
        }
    except Exception as err:
        raise handlerErr("bag -> c_bag_register_order -> %s" % err)
