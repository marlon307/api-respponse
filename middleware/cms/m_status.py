from pydantic import BaseModel, validator


class m_add_status(BaseModel):
    s_name: str

    @validator("s_name")
    def valid_status(cls, v: str):
        return v.title()
