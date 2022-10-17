from datetime import datetime
from models.database import execut_query
from models.model_address import qAddress


class sAddress:
    def s_add_address(json):
        json["cep"] = json["cep"].replace("-", "")
        id_insert = execut_query().insert(qAddress.q_insert_address(), json)
        return id_insert

    def s_get_address(user_id):
        list_address = execut_query().select(
            qAddress.q_get_address(), {"user_id": user_id}
        )
        return list_address

    def s_delete_address(user_id, id_address):
        execut_query().update(
            qAddress.q_delete_address(),
            {
                "delete_date": datetime.now(),
                "user_id": user_id,
                "address_id": id_address,
            },
        )
        return True
