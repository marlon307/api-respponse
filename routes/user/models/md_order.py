from pydantic import BaseModel
from datetime import datetime


class r_orderid(BaseModel):
    pass


class Order(BaseModel):
    id: int
    date_order: datetime
    status: str


class RListOrder(BaseModel):
    detail: str
    status: int
    orders: list[Order]


class RgOrder(BaseModel):
    detail: str
    status: int
    order: int
