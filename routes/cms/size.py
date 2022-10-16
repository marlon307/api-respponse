from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from middleware.cms.m_size import m_add_size
from controller.cms.controller_size import cSize
from middleware.m_auth import User, get_current_adm
from ..cms.models import Default

router = APIRouter(tags=["CMS"])


@router.post("/add_size", response_model=Default,status_code=201)
def add_size(data: m_add_size, current_user: User = Depends(get_current_adm)):
    return cSize.c_size(jsonable_encoder(data))
