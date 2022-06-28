from flask import request
from utility.credentials import valid_email, valid_psw

msgErr = {
    "msg": "Credenciais Inválidas.",
    "status": 400,
}, 400


def m_user():
    try:
        data = request.get_json()
        if request.path == "/createuser" and (
            data["name"] is None or len(data["name"]) < 4
        ):
            return msgErr
        # Falta válidar domino de email
        if data["email"] is None or valid_email(data["email"]) is not True:
            return msgErr
        if data["password"] is None or valid_psw(data["password"]) is not True:
            return msgErr

    except Exception as err:
        print(
            f"[Middleware Login] A requisição enviou %s, mas houve um problema [%s]"
            % (data, err)
        )
        return msgErr
