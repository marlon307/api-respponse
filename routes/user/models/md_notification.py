from pydantic import BaseModel, create_model


class DataNotification(BaseModel):
    id: int | None
