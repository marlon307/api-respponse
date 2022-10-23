from pydantic import BaseModel
from datetime import datetime


class ClsItemOrder(BaseModel):
    id: int
    size: str
    color: str
    price: float
    title: str
    quantity: int
    url_image: str
    color_name: str
    category_name: str


class ClsCarrier(BaseModel):
    code: str = None
    name_carrier: str
    delivery_value: float


class ClsAddress(BaseModel):
    uf: str
    city: str
    road: str
    zipcode: str
    district: str
    number_home: str
    name_delivery: str


class ClsOrder(BaseModel):
    id: int
    status_id: int
    date_order: datetime
    value_order: float
    address: ClsAddress
    carrier: ClsCarrier
    list_products: list[ClsItemOrder]


class ROrderId(BaseModel):
    detail: str
    status: int
    order: ClsOrder


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
