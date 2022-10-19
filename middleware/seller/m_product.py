from pydantic import BaseModel, validator
from uuid import UUID


class obj_size(BaseModel):
    colors_id: int
    sizes_id: int
    quantity: int
    price: float
    discount: int
    sku: str


class m_create_product(BaseModel):
    categorys_id: int
    gender_id: int
    id_user: UUID
    title: str
    subTitle: str
    warranty: int
    details: str
    specifications: str
    list_qtd: list[obj_size]

    @validator("id_user")
    def valid_uuid(cls, v: str):
        return str(v)
