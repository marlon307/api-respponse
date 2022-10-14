from pydantic import BaseModel


class add_bag(BaseModel):
    quantity: int
    option_product_id: int
    size: str


class del_bag(BaseModel):
    option_id: int
    size: str


class up_bag(BaseModel):
    qunatity: int
    option_id: int
    size: str


class r_order(BaseModel):
    address: int
    carrie: int
