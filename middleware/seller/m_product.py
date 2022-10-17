from fastapi import File
from pydantic import BaseModel, validator


class obj_size(BaseModel):
    colors_id: int
    sizes_id: int
    quantity: int
    price: float
    discount: int
    url_image: list[bytes] = File()
    sku: str


class m_create_product(BaseModel):
    categorys_id: int
    gender_id: int
    user_id: int
    title: str
    subTitle: str
    warranty: int
    details: str
    specifications: str
    list_qtd: list[obj_size]
