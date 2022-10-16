from datetime import datetime
from pydantic import BaseModel, EmailStr, UUID4
from .md_user import resp_user, resp_cUser
from .md_address import ListAdd
from .md_bag import rListBag

resp_user
resp_cUser
ListAdd
rListBag


class Default(BaseModel):
    detail: str
    status: int


class User(BaseModel):
    email: str | None = None
    full_name: str | None = None
    seller: bool | None = None
    admin: bool | None = None


class inf_uAuth(BaseModel):
    id_user: UUID4
    name: str
    email: EmailStr


class resp_auth(BaseModel):
    access_token: str
    token_type: str
    user: inf_uAuth
    detail: str
    exp: datetime
    status: int
