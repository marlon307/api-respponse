from functools import wraps
from flask import abort, request

msgErr = {
    "msg": "Não foi possivel inserir essa cor.",
    "status": 400,
}


def m_add_color(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            data = request.get_json()
            if "color_name" not in data or "color" not in data:
                abort(400, msgErr)
            return f(*args, **kwargs)

        except Exception as err:
            print(f"[Middleware add color] ( %s )" % (err))
            abort(400, msgErr)

    return decorated
