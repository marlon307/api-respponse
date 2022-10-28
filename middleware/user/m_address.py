from fastapi import Form
from pydantic import BaseModel


class m_addAddress(BaseModel):
    namedest: str
    city: str
    district: str
    state: str
    zipcode: str
    street: str
    number: str

    @classmethod
    def form_address(
        cls,
        namedest: str = Form(),
        city: str = Form(),
        district: str = Form(),
        state: str = Form(max_length=2),
        zipcode: str = Form(),
        street: str = Form(),
        number: str = Form(),
    ):
        return cls(
            namedest=namedest,
            city=city,
            district=district,
            state=state,
            zipcode=zipcode,
            street=street,
            number=number,
        )


class m_delAddress(BaseModel):
    id: int
