from flask import request
from utility.credentials import valid_email, valid_psw, valid_name

msgErr = {
    "msg": "Credenciais Inválidas.",
    "status": 400,
}, 400


class mUser:
    def __init__(self):
        self.data = request.get_json()
        self.err = {
            "msg": "Credenciais Inválidas.",
            "status": 400,
        }, 400

    def login() -> None | object:
        m = mUser()
        # Falta válidar domino de email
        if m.data["email"] is None or valid_email(m.data["email"]) is not True:
            return m.err
        if m.data["password"] is None or valid_psw(m.data["password"]) is not True:
            return m.err

    def register(self) -> None | object:
        m = mUser()
        if (
            m.data["name"] is None
            or len(m.data["name"]) < 4
            or valid_name(m.data["name"]) is not True
        ):
            return m.err
        # Falta válidar domino de email
        if m.data["email"] is None or valid_email(m.data["email"]) is not True:
            return m.err
        if m.data["password"] is None or valid_psw(m.data["password"]) is not True:
            return m.err


def m_user() -> None | object:
    try:
        data = request.get_json()
        if request.path == "/createuser" and (
            data["name"] is None
            or len(data["name"]) < 4
            or valid_name(data["name"]) is not True
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
