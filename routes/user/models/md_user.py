from datetime import date
from pydantic import BaseModel
from middleware.user.m_user import ModelEmail


class props_user(ModelEmail):
    name: str
    birthday: date
    cpf_cnpj: str
    gender_id: int
    tel: str
    cel: str
    umail: str


class resp_user(BaseModel):
    detail: str
    status: int
    response: props_user


# Create User
class resp_cUser(BaseModel):
    detail: str
    status: int
