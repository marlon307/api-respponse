from pydantic import BaseModel
from .md_product import ProductId, ListProduct,OptionProduct

ProductId
ListProduct
OptionProduct

class Default(BaseModel):
    detail: str
    status: int
