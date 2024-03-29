from datetime import date
from pydantic import BaseModel
from middleware.user.m_user import ModelEmail


class props_user(ModelEmail):
    name: str
    birthday: date | None
    cpf: str | None
    gender_id: int | None
    tel: str | None
    cel: str | None
    email: str


class resp_user(BaseModel):
    detail: str
    status: int
    response: props_user


# Create User
class resp_cUser(BaseModel):
    detail: str
    status: int
