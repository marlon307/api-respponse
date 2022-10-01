from pydantic import BaseModel, EmailStr, validator
from datetime import date
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


class m_login(BaseModel):
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


class m_psw(BaseModel):
    password: str

    @validator("password")
    def valid_psw(cls, v: str):
        if valid_psw(v) is not True:
            raise ValueError("Senha inválida.")
        return v.title()


class m_update_user(BaseModel):
    name: str
    cel: str
    te: str
    date: date
    doc: str
    gender: int

    @validator("name")
    def valid_name(cls, v: str):
        if valid_name(v) is not True:
            raise ValueError("Nome inválido.")
        return v.title()
