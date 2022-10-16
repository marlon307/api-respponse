from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from middleware.cms.m_category import m_add_category
from controller.cms.controller_category import cCategory
from middleware.m_auth import get_current_adm, User
from .models import Default

router = APIRouter(tags=["CMS"])


@router.post("/create_category", response_model=Default, status_code=201)
def add_category(data: m_add_category, current_user: User = Depends(get_current_adm)):
    return cCategory.c_category(jsonable_encoder(data))
