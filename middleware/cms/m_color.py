from pydantic import BaseModel, validator


class m_add_color(BaseModel):
    color_name: str
    color: str

    @validator("color_name")
    def valid_color_name(cls, v):
        return v.title()
