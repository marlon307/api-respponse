from fastapi import APIRouter, Depends
from middleware.cms.m_gender import m_add_gender
from controller.cms import controller_gender
from middleware.m_auth import User, get_current_adm
from ..cms.models import Default

router = APIRouter(tags=["CMS"])


@router.post("/create_gender", response_model=Default, status_code=201)
def add_gender(data: m_add_gender, current_user: User = Depends(get_current_adm)):
    return controller_gender.c_gender(data.dict())
