from datetime import datetime
from pydantic import BaseModel, validator, UUID4
from middleware.user.m_user import ModelEmail
from utility.format_doc import format_email
from .md_user import resp_user, resp_cUser
from .md_address import ListAdd
from .md_bag import ListBag
from .md_order import ROrderId, RListOrder, RgOrder


class Default(BaseModel):
    detail: str
    status: int


resp_user = resp_user
resp_cUser = resp_cUser
ListAdd = ListAdd
ListBag = ListBag
RListOrder = RListOrder
RgOrder = RgOrder
ROrderId = ROrderId


class resp_auth(BaseModel):
    access_token: str
    token_type: str
    detail: str
    exp: datetime
    status: int
