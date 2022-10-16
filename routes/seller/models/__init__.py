from pydantic import BaseModel


class Default(BaseModel):
    detail: str
    status: int
