from datetime import datetime
from models.database import execut_query
from models import model_address


def s_add_address(json):
    json["cep"] = json["cep"].replace("-", "")
    id_insert = execut_query(model_address.q_insert_address).insert(json)
    return id_insert


def s_get_address(user_id):
    list_address = execut_query(model_address.q_get_address).select(
        {"user_id": user_id}
    )
    return list_address


def s_delete_address(user_id, id_address):
    execut_query(model_address.q_delete_address).update(
        {
            "delete_date": datetime.now(),
            "user_id": user_id,
            "address_id": id_address,
        },
    )
    return True
