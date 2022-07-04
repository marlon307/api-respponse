from flask import request
import os


def request_front():
    header = request.headers
    if header["host"] != os.getenv("API_HOST"):
        return {
            "msg": "Requisição incorreta.",
            "status": 500,
        }, 500
    pass
