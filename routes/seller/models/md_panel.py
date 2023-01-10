from pydantic import BaseModel
from ...user.models.md_address import AddressProps


class SettingsPanelSeller(BaseModel):
    store_name: str
    cnpj: str
    ie: str
    address: AddressProps
