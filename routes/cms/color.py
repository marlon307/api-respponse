from fastapi import APIRouter, Depends
from middleware.cms.m_color import m_add_color
from controller.cms import controller_color
from middleware.m_auth import User, get_current_adm
from .models import Default


router = APIRouter(tags=["CMS"])


@router.post("/add_color", response_model=Default, status_code=201)
def add_color(data: m_add_color, current_user: User = Depends(get_current_adm)):
    return controller_color.c_color(data.dict())
