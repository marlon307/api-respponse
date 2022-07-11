from flask import request


def request_front():
    header = request.headers

    if header["host"] != "localhost:5000":
        return {
            "msg": "Requisição incorreta.",
            "status": 500,
        }, 500
    pass
