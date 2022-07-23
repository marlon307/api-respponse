from functools import wraps
from flask import request

msgErr = {
    "msg": "Não foi possivel inserir essa cor.",
    "status": 400,
}, 400


def m_add_color(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            data = request.get_json()
            if data["color_name"] is None and data["color"] is None:
                return msgErr
            return f(*args, **kwargs)

        except Exception as err:
            print(
                f"[Middleware add color] A requisição enviou ( %s ), mas houve um problema"
                % (err)
            )
            return msgErr

    return decorated
