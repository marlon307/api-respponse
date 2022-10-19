from pydantic import BaseModel, validator


class m_add_category(BaseModel):
    c_image: str
    c_name: str
    c_title: str
    c_path: str
    c_color: str

    @validator("c_title")
    def valid_c_title(cls, v):
        return v.title()

    @validator("c_name")
    def valid_c_name(cls, v):
        return v.title()
