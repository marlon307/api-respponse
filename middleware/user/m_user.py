from fastapi import Form, HTTPException
from pydantic import BaseModel, validator
from datetime import date
from utility.credentials import valid_email, valid_psw, valid_name
from utility.valid_cpf import cpf_validate


class ModelUsrName(BaseModel):
    name: str

    @validator("name")
    def validator_name(cls, v):
        if valid_name(v) is not True:
            raise HTTPException(
                detail={"detail": "Nome inválido.", "status": 400},
                status_code=400,
            )
        return v.title()


class ModelEmail(BaseModel):
    email: str

    @validator("email")
    def validator_email(cls, v):
        if valid_email(v) is not True:
            raise HTTPException(
                detail={"detail": "Email inválido.", "status": 400},
                status_code=400,
            )
        return v

    @classmethod
    def form_email(cls, email: str = Form()):
        return cls(email=email)


class ModelPsw(BaseModel):
    password: str

    @validator("password")
    def validator_password(cls, v):
        if valid_psw(v) is not True:
            raise HTTPException(
                detail={"detail": "Senha inválida.", "status": 400},
                status_code=400,
            )
        return v


class ModelDOC(BaseModel):
    doc: str

    @validator("doc")
    def validator_doc(cls, v):
        if cpf_validate(v) is not True:
            raise HTTPException(
                detail={
                    "detail": "CPF inválido.",
                    "field": "doc",
                    "status": 400,
                },
                status_code=400,
            )
        return v


class ModelRegister(ModelUsrName, ModelEmail, ModelPsw):
    @classmethod
    def fields_register(
        cls,
        name: str = Form(),
        email: str = Form(),
        password: str = Form(),
    ):
        return cls(name=name, email=email, password=password)


class ModelUpUser(ModelUsrName, ModelDOC):
    date: date
    cel: str
    tel: str
    gender: int

    @classmethod
    def fields_update(
        cls,
        name: str = Form(),
        date: date = Form(),
        doc: str = Form(),
        gender: int = Form(),
        cel: str = Form(),
        tel: str = Form(),
    ):
        return cls(name=name, cel=cel, tel=tel, date=date, doc=doc, gender=gender)
