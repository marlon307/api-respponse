from pydantic import BaseModel

from middleware.seller.m_settings import Boxes
from ...user.models.md_address import AddressProps


class Settings(BaseModel):
    store_name: str
    cnpj: str
    ie: str
    obs: str
    address: AddressProps
    boxes: list[Boxes]


class SettingsPanelSeller(BaseModel):
    settings: Settings
    status: int
    detail: str
