from fastapi import Form
from pydantic import BaseModel, validator
from datetime import date
from utility.credentials import valid_email, valid_psw, valid_name
from utility.valid_cpf import cpf_validate


class ModelUsrName(BaseModel):
    name: str

    @validator("name")
    def validator_name(cls, v):
        if valid_name(v) is not True:
            raise ValueError("Nome inválido.")
        return v.title()


class ModelEmail(BaseModel):
    email: str

    @validator("email")
    def validator_email(cls, v):
        if valid_email(v) is not True:
            raise ValueError("Email inválido.")
        return

    @classmethod
    def form_email(cls, email: str = Form()):
        return cls(email=email)


class ModelPsw(BaseModel):
    password: str

    @validator("password")
    def validator_password(cls, v):
        if valid_psw(v) is not True:
            raise ValueError("Senha inválida.")
        return v


class ModelRegister(ModelUsrName):
    username: str
    password: str


class ModelUpUser(ModelUsrName):
    cel: str
    tel: str
    date: date
    doc: str
    gender: int

    @validator("doc")
    def validator_doc(cls, v):
        if cpf_validate(v) is not True:
            raise ValueError("Documento inválido.")
        return v
