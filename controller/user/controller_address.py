from fastapi import status, HTTPException
from service.user import service_address

msgErr500 = HTTPException(
    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    detail="Server error.",
)


def add_address(json, c_user):
    print(type(json))
    try:
        json["user_id"] = c_user.id_user
        id_addres = service_address.s_add_address(json)

        return {
            "detail": "Endereço adicionado.",
            "address": id_addres,
            "status": 201,
        }
    except Exception as err:
        print("address -> add_address ->", err)
        raise msgErr500


def get_address(data):
    try:
        list_address = service_address.s_get_address(data.id_user)
        return {
            "detail": "Lista de endereço.",
            "address": list_address,
            "status": 200,
        }
    except Exception as err:
        print("address -> get_address ->", err)
        raise msgErr500


def delete_address(json, id_user):
    try:
        service_address.s_delete_address(id_user, json["id"])
        return {
            "detail": "Endereço excluído.",
            "status": 200,
        }
    except Exception as err:
        print("address -> delete_address ->", err)
        raise msgErr500
