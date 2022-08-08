from models.database import execut_query
from models.model_address import qAddress


class sAddress:
    def s_add_address(json):
        json["cep"] = json["cep"].replace("-", "")
        execut_query.insert(qAddress.q_insert_address(), json)
        return True

    def s_get_address(user_id):
        list_address = execut_query.select(
            qAddress.q_get_address(), {"user_id": user_id}
        )
        return list_address

    def s_delete_address(user_id, id_address):
        execut_query.delete(
            qAddress.q_delete_address(),
            {
                "user_id": user_id,
                "address_id": id_address,
            },
        )
        return True
