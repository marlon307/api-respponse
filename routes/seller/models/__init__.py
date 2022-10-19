from pydantic import BaseModel
from .md_product import ProductId, ListProduct

ProductId
ListProduct


class Default(BaseModel):
    detail: str
    status: int
