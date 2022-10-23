from datetime import datetime
from pydantic import BaseModel, UUID4
from middleware.user.m_user import ModelEmail
from .md_user import resp_user, resp_cUser
from .md_address import ListAdd
from .md_bag import ListBag
from .md_order import r_orderid, RListOrder, RgOrder


class Default(BaseModel):
    detail: str
    status: int


resp_user = resp_user
resp_cUser = resp_cUser
ListAdd = ListAdd
ListBag = ListBag
r_orderid = r_orderid
RListOrder = RListOrder
RgOrder = RgOrder


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
