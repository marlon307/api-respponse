from fastapi import APIRouter, Depends
from ..cms.models import Default
from middleware.m_auth import User, get_current_adm
from controller.cms import controller_carries


router = APIRouter(tags=["CMS", "CARRIER"])


@router.post("/refresh_carriers", response_model=Default, status_code=201)
def refresh_carrier(current_user: User = Depends(get_current_adm)):
    return controller_carries.c_refresh_carries()
