from pydantic import BaseModel, EmailStr, validator
from functools import wraps
from utility.credentials import valid_email, valid_psw, valid_name
from utility.format_doc import format_cpf
from utility.valid_cpf import cpf_validate

msgErr = {
    "msg": "Credenciais Inválidas.",
    "status": 400,
}, 400


class m_register(BaseModel):
    name: str
    email: EmailStr
    password: str

    @validator("email")
    def valid_email(cls, v: str):
        if valid_email(v) is not True:
            raise ValueError("Email inválido.")
        return v.title()

    @validator("password")
    def valid_psw(cls, v: str):
        if valid_psw(v) is not True:
            raise ValueError("Senha inválida.")
        return v.title()

    @validator("name")
    def valid_name(cls, v: str):
        if valid_name(v) is not True:
            raise ValueError("Nome inválido.")
        return v.title()


class m_email(BaseModel):
    email: EmailStr

    @validator("email")
    def valid_email(cls, v: str):
        if valid_email(v) is not True:
            raise ValueError("Email inválido.")
        return v.title()


def m_login(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            data = request.get_json()

            if (
                "email" not in data
                or data["email"] is None
                or valid_email(data["email"]) is not True
            ):
                return msgErr

            if (
                "password" not in data
                or data["password"] is None
                or valid_psw(data["password"]) is not True
            ):
                return msgErr

            return f(*args, **kwargs)

        except Exception as err:
            print(f"[Middleware Login] ( %s ) [%s]" % (data, err))
            return msgErr

    return decorated


def m_psw(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            data = request.get_json()
            if (
                "password" not in data
                or data["password"] is None
                or valid_psw(data["password"]) is not True
            ):
                return msgErr
            return f(*args, **kwargs)

        except Exception as err:
            print(f"[Middleware Login] ( %s )" % (err))
            return msgErr

    return decorated


def m_update_user(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            list_key_onj = ["cel", "date", "doc", "gender", "name", "tel"]
            data = request.get_json()

            for key in data:
                if key not in list_key_onj:
                    return msgErr
            if (
                valid_name(data["name"]) is not True
                or cpf_validate(data["doc"]) is False
            ):
                return msgErr

            return f(*args, **kwargs)

        except Exception as err:
            print(f"[Middleware update_user] ( %s )" % (err))
            return msgErr

    return decorated
