from pydantic import BaseModel, validator


class m_add_gender(BaseModel):
    g_initials: str
    g_name: str

    @validator("g_initials")
    def valid_initial(cls, v: str):
        return v.title()

    @validator("g_name")
    def valid_name(cls, v: str):
        return v.title()
