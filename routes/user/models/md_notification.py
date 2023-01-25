from pydantic import BaseModel


class DataNotification(BaseModel):
    id: int | None
