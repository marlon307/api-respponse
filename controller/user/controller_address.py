from service.user import service_address
from utility.handleErr import handlerErr


def add_address(json, c_user):
    try:
        json["user_id"] = c_user.id_user
        id_addres = service_address.s_add_address(json)

        return {
            "detail": "Endereço adicionado.",
            "id": id_addres,
            "status": 201,
        }
    except Exception as err:
        raise handlerErr("address -> add_address -> %s" % err)


def get_address(data):
    try:
        list_address = service_address.s_get_address(data.id_user)
        return {
            "detail": "Lista de endereço.",
            "address": list_address,
            "status": 200,
        }
    except Exception as err:
        raise handlerErr("address -> get_address -> %s" % err)


def delete_address(json, id_user):
    try:
        service_address.s_delete_address(id_user, json["id"])
        return {
            "detail": "Endereço excluído.",
            "status": 200,
        }
    except Exception as err:
        raise handlerErr("address -> delete_address -> %s" % err)
