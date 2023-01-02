from pydantic import BaseModel


class add_bag(BaseModel):
    quantity: int
    product_option: int
    size: str


class del_bag(BaseModel):
    product_option: int
    size: str


class up_bag(BaseModel):
    quantity: int
    product_option: int
    size: str


class r_order(BaseModel):
    address: int
    carrie: int
    shipping: float
    method_pay: str
    card: dict | None


class Carriers(BaseModel):
    zipcode: str = "Exemplo: 12345678"
