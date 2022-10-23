from pydantic import BaseModel


class r_orderid(BaseModel):
    pass


class r_order(BaseModel):
    pass


class RgOrder(BaseModel):
    detail: str
    status: int
    order: int
