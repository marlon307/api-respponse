from flask import request
from utility.m_credentials import valid_email, valid_psw
from utility.generat_id import generate_id
import uuid

msgErr = {
    "msg": "Credenciais Inválidas.",
    "status": 400,
}, 400


def m_user():
    try:
        data = request.get_json()

        if data["name"] is None or len(data["name"]) < 4:
            return msgErr
        if data["email"] is None or valid_email(data["email"]) is not True:
            return msgErr
        if data["password"] is None or valid_psw(data["password"]) is not True:
            return msgErr

    except Exception as err:
        print(
            f"A requisição enviou [%s], mas não foi encontrado o chave [%s]"
            % (data, err)
        )
        return msgErr
