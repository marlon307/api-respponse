from pydantic import BaseModel


class add_bag(BaseModel):
    quantity: int
    product_option: int
    size: str


class del_bag(BaseModel):
    product_option: int
    size: str


class up_bag(BaseModel):
    qunatity: int
    option_id: int
    size: str


class r_order(BaseModel):
    address: int
    carrie: int
