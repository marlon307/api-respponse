from pydantic import BaseModel
from .md_address import AddressProps


class ItemBag(BaseModel):
    id: int
    size: str
    color: str
    price: float
    title: str
    opt_id: int
    discount: int
    quantity: int
    url_image: str
    color_name: str
    category_name: str
    oldPrice: float


class InfoBag(BaseModel):
    list_b: list[ItemBag]
    list_add: list[AddressProps]


class ListBag(BaseModel):
    detail: str
    status: int
    infobag: InfoBag
