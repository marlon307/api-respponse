from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from middleware.cms.m_status import m_add_status
from controller.cms import controller_status
from middleware.m_auth import User, get_current_adm
from ..cms.models import Default


router = APIRouter(tags=["CMS"])


@router.post("/add_status", response_model=Default, status_code=201)
def add_status(data: m_add_status, current_user: User = Depends(get_current_adm)):
    return controller_status.c_status(jsonable_encoder(data))
