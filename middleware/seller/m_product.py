from pydantic import BaseModel, validator, UUID4


class sizes(BaseModel):
    id: int
    quantity: int


class obj_option(BaseModel):
    id: int
    sizes_id: list[sizes]
    color: str
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
    list_qtd: list[obj_option]

    @validator("id_user")
    def valid_uuid(cls, v):
        return str(v)
