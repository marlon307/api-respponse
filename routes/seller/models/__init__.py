from pydantic import BaseModel


class Default(BaseModel):
    detail: str
    status: int


class ListImage(BaseModel):
    imgid: int
    urlImg: str
    option_id: int


class ListOption(BaseModel):
    idc: int
    color: str
    price: float
    discount: int
    colorName: str
    option_id: int
    oldPrice: float
    sizes: dict
    images: list[ListImage]


class Product(BaseModel):
    id: int
    title: str
    details: str
    specifications: str
    category_name: str
    list_options: list[ListOption]


class ProductId(BaseModel):
    product: Product
    detail: str
    status: int
