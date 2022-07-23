from functools import wraps
from flask import request

msgErr = {
    "msg": "Não foi possivel cirar essa categoria.",
    "status": 400,
}, 400


def m_add_category(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            data = request.get_json()
            if (
                data["c_image"] is None
                and data["c_name"] is None
                and data["c_title"] is None
                and data["c_path"] is None
                and data["c_color"] is None
            ):
                return msgErr
            return f(*args, **kwargs)

        except Exception as err:
            print(f"[Middleware add category] ( %s )" % (err))
            return msgErr

    return decorated
