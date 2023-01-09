from fastapi import Form
from pydantic import BaseModel


class m_addAddress(BaseModel):
    name_delivery: str
    city: str
    district: str
    state: str
    zipcode: str
    street: str
    number_home: str
    complement: str

    @classmethod
    def form_address(
        cls,
        name_delivery: str = Form(),
        city: str = Form(),
        district: str = Form(),
        state: str = Form(max_length=2),
        zipcode: str = Form(),
        street: str = Form(),
        number_home: str = Form(),
        complement: str = Form(),
    ):
        return cls(
            name_delivery=name_delivery,
            city=city,
            district=district,
            state=state,
            zipcode=zipcode,
            street=street,
            number_home=number_home,
            complement=complement,
        )
