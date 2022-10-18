from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from middleware.cms.m_category import m_add_category
from controller.cms import controller_category
from middleware.m_auth import get_current_adm, User
from .models import Default

router = APIRouter(tags=["CMS"])


@router.post("/create_category", response_model=Default, status_code=201)
def add_category(data: m_add_category, current_user: User = Depends(get_current_adm)):
    return controller_category.c_category(jsonable_encoder(data))
