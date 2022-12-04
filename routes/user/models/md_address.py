from pydantic import BaseModel
from middleware.user.m_address import m_addAddress


class AddressProps(m_addAddress):
    id: int


class ListAdd(BaseModel):
    detail: str
    status: int
    address: list[AddressProps]


class AddAddress(BaseModel):
    id: int
    detail: str
    status: int
