from pydantic import BaseModel
from .md_product import ProductId, ListProduct, OptionProduct
from .md_panel import SettingsPanelSeller

ProductId
ListProduct
OptionProduct
SettingsPanelSeller


class Default(BaseModel):
    detail: str
    status: int
