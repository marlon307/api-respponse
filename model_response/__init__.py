from datetime import datetime
from pydantic import BaseModel, EmailStr, UUID4
from model_response.user import user

resp_user = user.resp_user


class inf_uAuth(BaseModel):
    id_user: UUID4
    name: str
    email: EmailStr


class resp_auth(BaseModel):
    access_token: str
    token_type: str
    user: inf_uAuth
    detail: str
    exp: datetime
    status: int
