from pydantic import BaseModel


class m_addAddress(BaseModel):
    name_delivery: str
    city: str
    district: str
    uf: str
    cep: str
    road: str
    number_home: str


class m_delAddress(BaseModel):
    id: int
