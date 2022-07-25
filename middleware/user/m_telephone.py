from ast import Num
from functools import wraps
from flask import request

msgErr = {
    "msg": "Dados enviados inválidos.",
    "status": 400,
}, 400


def m_telephone(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            data = request.get_json()
            if (
                "n_phones" not in data
                or isinstance(data["n_phones"], list) == False
                or len(data["n_phones"]) > 2
            ):
                return msgErr

            for obj in data["n_phones"]:
                if "n_phone" not in obj or isinstance(obj["n_phone"], int) == False:
                    return msgErr

            return f(*args, **kwargs)

        except Exception as err:
            print(f"[Middleware telephone] ( %s ) [%s]" % (data, err))
            return msgErr

    return decorated
