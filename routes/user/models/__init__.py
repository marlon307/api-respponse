from datetime import datetime
from wsgiref.validate import validator
from pydantic import BaseModel, UUID4
from middleware.user.m_user import ModelEmail

from utility.credentials import valid_email
from .md_user import resp_user, resp_cUser
from .md_address import ListAdd
from .md_bag import rListBag
from .md_order import r_orderid, r_order

resp_user = resp_user
resp_cUser = resp_cUser
ListAdd = ListAdd
rListBag = rListBag
r_orderid = r_orderid
r_order = r_order


class Default(BaseModel):
    detail: str
    status: int


class inf_uAuth(ModelEmail):
    id_user: UUID4
    name: str


class resp_auth(BaseModel):
    access_token: str
    token_type: str
    user: inf_uAuth
    detail: str
    exp: datetime
    status: int
