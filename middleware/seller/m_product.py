from ast import Num
from functools import wraps
from flask import request

msgErr = {
    "msg": "Não foi possível criar este produto.",
    "status": 400,
}, 400
list_keys = [
    "categorys_id",
    "gender_id",
    "user_id",
    "title",
    "subTitle",
    "warranty",
    "details",
    "specifications",
    "list_qtd",
]
list_keys_size = [
    "colors_id",
    "sizes_id",
    "quantity",
    "price",
    "discount",
    "url_image",
    "sku",
]


def chek_list(list_size: list):
    for object_size in list_size:
        if (
            False in [x in list_keys_size for x in object_size]
            or isinstance(object_size["colors_id"], int) is False
            or isinstance(object_size["sizes_id"], int) is False
            or isinstance(object_size["quantity"], int) is False
            or isinstance(object_size["price"], float) is False
            or isinstance(object_size["discount"], int) is False
            or isinstance(object_size["url_image"], str) is False
            or isinstance(object_size["sku"], str) is False
        ):
            return False
    return True


def m_create_product(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            data = request.get_json()
            if (
                (False in [x in list_keys for x in data]) is False
                and isinstance(data["categorys_id"], int)
                and isinstance(data["gender_id"], int)
                and isinstance(data["user_id"], int)
                and isinstance(data["title"], str)
                and isinstance(data["subTitle"], str)
                and isinstance(data["warranty"], int)
                and isinstance(data["details"], str)
                and isinstance(data["specifications"], str)
                and isinstance(data["list_qtd"], list)
                and chek_list(data["list_qtd"])
            ):
                return f(*args, **kwargs)
            return msgErr

        except Exception as err:
            print(f"[Middleware create product] ( %s )" % (err))
            return msgErr

    return decorated
