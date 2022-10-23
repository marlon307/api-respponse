from pydantic import BaseModel
from .md_address import AddressProps
from .md_order import ClsItemOrder


class ItemBag(ClsItemOrder):
    discount: int
    opt_id: int
    oldPrice: float


class InfoBag(BaseModel):
    list_b: list[ItemBag]
    list_add: list[AddressProps]


class ListBag(BaseModel):
    detail: str
    status: int
    infobag: InfoBag
