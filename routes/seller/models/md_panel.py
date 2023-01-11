from pydantic import BaseModel
from ...user.models.md_address import AddressProps


class Settings(BaseModel):
    store_name: str
    cnpj: str
    ie: str
    obs: str
    address: AddressProps


class SettingsPanelSeller(BaseModel):
    settings: Settings
    status: int
    detail: str
