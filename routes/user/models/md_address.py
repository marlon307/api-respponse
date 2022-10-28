from pydantic import BaseModel


class AddressProps(BaseModel):
    id: int
    name_delivery: str
    city: str
    district: str
    uf: str
    cep: str
    road: str
    number_home: str


class ListAdd(BaseModel):
    detail: str
    status: int
    address: list[AddressProps]


class AddAddress(BaseModel):
    id: int
    detail: str
    status: int
