import json
from fastapi import Form
from pydantic import BaseModel, validator

example = [{"width": "0", "height": "0", "length": "0", "weight": "0"}]


class Boxes(BaseModel):
    id: int | None
    height: float
    length: float
    weight: float
    width: float


class ListBoxes(BaseModel):
    boxes: list[Boxes]


class SettingsSeller(BaseModel):
    store_name: str
    address: int
    ie: int
    obs: str
    cnpj: int
    listboxes: str

    @validator("listboxes")
    def convert_json_boxes(cls, v):
        data = json.loads(v)
        ListBoxes(boxes=data)
        return data

    @classmethod
    def fields_settings(
        cls,
        store_name: str = Form(),
        cnpj: str = Form(),
        ie: int = Form(),
        address: int = Form(),
        obs: str = Form(),
        listboxes: str = Form(
            default=str(example),
            description="* Copie as informaçoes do input e altere os valores mantendo o formato (STRING/JSON)",
        ),
    ):
        return cls(
            store_name=store_name,
            cnpj=cnpj,
            ie=ie,
            address=address,
            obs=obs,
            listboxes=listboxes,
        )
