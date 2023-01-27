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
    payment: str
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


class OrderIdSeller(BaseModel):
    detail: str
    status: int
    order: ClsOrder


class ErrOder(BaseModel):
    product_id: int
    options_product: int


class OrderCard(BaseModel):
    number_order: int


class OrderPix(BaseModel):
    number_order: int
    date_of_expiration: datetime
    qr_code: str
    transaction_amount: float
    qr_code_base64: str


class RgOrder(BaseModel):
    detail: str
    status: int
    order: OrderPix | OrderCard | ErrOder
