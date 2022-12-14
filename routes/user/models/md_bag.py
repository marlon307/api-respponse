from pydantic import BaseModel
from .md_address import AddressProps
from .md_order import ClsItemOrder


class Shipping(BaseModel):
    id: int
    name_carrier: str
    price: float
    toDate: int


class ItemBag(ClsItemOrder):
    opt_id: int
    discount: float


class InfoBag(BaseModel):
    list_b: list[ItemBag]
    main_add: AddressProps | dict
    shipping_company: list[Shipping]


class ListBag(BaseModel):
    detail: str
    status: int
    infobag: InfoBag
