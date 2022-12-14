from datetime import datetime
from models.database import MySQLCnn
from models import model_address


def s_add_address(json):
    json["zipcode"] = json["zipcode"].replace("-", "")
    execut_query = MySQLCnn()
    id_insert = execut_query.insert(model_address.q_insert_address, json)
    execut_query.finishExecution()
    return id_insert


def s_get_address(user_id):
    execut_query = MySQLCnn()
    list_address = execut_query.select(
        model_address.q_get_address, {"user_id": user_id}
    )
    execut_query.finishExecution()
    return list_address


def s_delete_address(user_id, id_address):
    execut_query = MySQLCnn()
    execut_query.update(
        model_address.q_delete_address,
        {
            "delete_date": datetime.now(),
            "user_id": user_id,
            "address_id": id_address,
        },
    )
    execut_query.finishExecution()
    return True
