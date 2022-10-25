from fastapi import APIRouter, Depends
from controller.seller import c_orders
from middleware.m_auth import User, get_current_adm
from ..user.models.md_order import RListOrder


router = APIRouter(tags=["SELLER"])


@router.get("/seller/orders/{status}", response_model=RListOrder)
def list_order_seller(status: int, current_user: User = Depends(get_current_adm)):
    return c_orders.seller_orders(status, current_user)
