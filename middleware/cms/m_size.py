from functools import wraps
from flask import request, abort

msgErr = {
    "msg": "Não foi possivel inserir este tamanho.",
    "status": 400,
}


def m_add_size(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            data = request.get_json()
            if "value_size" not in data:
                abort(400, msgErr)
            return f(*args, **kwargs)

        except Exception as err:
            print(f"[Middleware add size] ( %s )" % (err))
            abort(400, msgErr)

    return decorated
