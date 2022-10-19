from pydantic import BaseModel, validator, UUID4


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
    id_user: UUID4
    title: str
    subTitle: str
    warranty: int
    details: str
    specifications: str
    list_qtd: list[obj_size]

    @validator("id_user")
    def valid_uuid(cls, v):
        return str(v)
