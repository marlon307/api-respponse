from datetime import datetime
from pydantic import BaseModel, EmailStr, UUID4
from .md_user import resp_user, resp_cUser
from .md_address import ListAdd
from .md_bag import rListBag
from .md_order import r_orderid, r_order

resp_user
resp_cUser
ListAdd
rListBag
r_orderid
r_order


class Default(BaseModel):
    detail: str
    status: int


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
