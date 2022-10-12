from functools import wraps
from flask import request

msgErr = {
    "detail": "Não foi possivel cirar essa categoria.",
    "status": 400,
}


def m_add_category(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            data = request.get_json()
            if (
                "c_image" not in data
                or "c_name" not in data
                or "c_title" not in data
                or "c_path" not in data
                or "c_color" not in data
            ):
                return msgErr
            return f(*args, **kwargs)

        except Exception as err:
            print(f"[Middleware add category] ( %s )" % (err))
            return msgErr

    return decorated
