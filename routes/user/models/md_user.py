from datetime import date
from pydantic import BaseModel, EmailStr


class props_user(BaseModel):
    name: str
    email: EmailStr
    birthday: date | None
    cpf_cnpj: str | None
    gender_id: int | None
    tel: str | None
    cel: str | None


class resp_user(BaseModel):
    detail: str
    status: int
    response: props_user

# Create User
class resp_cUser(BaseModel):
    detail: str
    status: int
    response: props_user
