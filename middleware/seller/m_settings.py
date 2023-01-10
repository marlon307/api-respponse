from fastapi import Form
from pydantic import BaseModel


class SettingsSeller(BaseModel):
    store_name: str
    address: int
    ie: int
    cnpj: int

    @classmethod
    def fields_settings(
        cls,
        store_name: str = Form(),
        cnpj: str = Form(),
        ie: int = Form(),
        address: int = Form(),
    ):
        return cls(store_name=store_name, cnpj=cnpj, ie=ie, address=address)
