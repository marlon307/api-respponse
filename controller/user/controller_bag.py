from service.user import service_bag
from utility.handleErr import handlerErr, JSONResponse, status


def c_add_bag(json, c_user):
    try:
        json["user_id"] = c_user.id_user
        product_id = service_bag.add_bag(json)

        return {
            "detail": "Produto adicionado a sacola.",
            "item_bag": product_id,
            "status": 201,
        }
    except Exception as err:
        raise handlerErr("bag -> c_add_bag -> %s" % err)


def c_list_bag(c_user):
    try:
        list_items = service_bag.list_bag(c_user.id_user)
        if list_items is not False:
            return {
                "detail": "Lista da sacola.",
                "infobag": list_items,
                "status": 200,
            }
        return JSONResponse(
            content={
                "detail": "Sacola vazia.",
                "status": status.HTTP_200_OK,
            },
            status_code=status.HTTP_200_OK,
        )
    except Exception as err:
        raise handlerErr("bag -> c_list_bag -> %s" % err)


def c_bag_update_quantity(json, c_user):
    try:
        json["user_id"] = c_user.id_user
        service_bag.update_quantity_bag(json)

        return {
            "detail": "Quantidade atualizada.",
            "status": 200,
        }
    except Exception as err:
        raise handlerErr("bag -> c_update_bag -> %s" % err)


def c_bag_delete(json, c_user):
    try:
        json["user_id"] = c_user.id_user
        service_bag.s_delete_item_bag(json)
        return {
            "detail": "Produto removido da sacola.",
            "status": 200,
        }
    except Exception as err:
        raise handlerErr("bag -> c_delete_bag -> %s" % err)


def c_bag_register_order(json, c_user, task):
    try:
        json["p_userid"] = c_user.id_user
        order = service_bag.register_order(json)
        task.add_task(service_bag.recalc_carrier, json, order)

        if "number_order" in order:
            return {
                "detail": "Pedido realizado.",
                "order": order,
                "status": 200,
            }
        return JSONResponse(
            content={
                "detail": "Um item da sacola não está disponível nessa quantidade.",
                "status": status.HTTP_409_CONFLICT,
                "order": {
                    "product_id": order["product_id"],
                    "options_product": order["options_product_id"],
                },
            },
            status_code=status.HTTP_409_CONFLICT,
        )
    except Exception as err:
        raise handlerErr("bag -> c_bag_register_order -> %s" % err)


def c_bag_calc_shipping(json, c_user):
    try:
        json["user_id"] = c_user.id_user
        carriers = service_bag.s_calc_shipping(json)
        return {
            "carriers": carriers,
            "detail": "Tranportadora disponíveis.",
            "status": 200,
        }
    except Exception as err:
        raise handlerErr("bag -> c_calc_shipping -> %s" % err)
