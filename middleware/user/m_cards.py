from functools import wraps
from flask import request

msgErr = {
    "detail": "Dados enviados inválidos.",
    "status": 400,
}, 400


def m_cards(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            data = request.get_json()
            if (
                "c_name" not in data
                or "c_number" not in data
                or "c_exp" not in data
                or "c_flag" not in data
                or "c_cpf" not in data
                or "c_birthday" not in data
            ):
                return msgErr

            for key in data:
                if data[key] is None or data[key] == "":
                    return msgErr
            return f(*args, **kwargs)

        except Exception as err:
            print(f"[Middleware cards] ( %s ) [%s]" % (data, err))
            return msgErr

    return decorated
