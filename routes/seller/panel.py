from fastapi import APIRouter, Depends
from controller.seller import c_panel
from middleware.m_auth import User, get_current_adm


router = APIRouter(tags=["SELLER"])


@router.get(
    "/panel/seller/",
    # response_model=RListOrder,
)
def panel_seller(current_user: User = Depends(get_current_adm)):
    return c_panel.seller_panel(current_user)
