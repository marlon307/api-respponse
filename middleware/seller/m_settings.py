from fastapi import Form
from pydantic import BaseModel


class SettingsSeller(BaseModel):
    store_name: str
    address: int
    ie: int
    obs: str
    cnpj: int

    @classmethod
    def fields_settings(
        cls,
        store_name: str = Form(),
        cnpj: str = Form(),
        ie: int = Form(),
        address: int = Form(),
        obs: str = Form(),
    ):
        return cls(store_name=store_name, cnpj=cnpj, ie=ie, address=address, obs=obs)
