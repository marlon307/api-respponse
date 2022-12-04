from pydantic import BaseModel, validator


class m_add_size(BaseModel):
    value_size: str

    @validator("value_size")
    def valid_size(cls, v):
        return v.title()
