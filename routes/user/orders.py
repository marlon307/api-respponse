from fastapi import APIRouter, Depends
from middleware.m_auth import User, get_current_user
from controller.user import controller_order
from ..user.models import RListOrder, r_orderid

router = APIRouter(tags=["USER"])


@router.get("/order", response_model=RListOrder)
def get_orders(current_user: User = Depends(get_current_user)):
    return controller_order.get_orders(current_user)


@router.get("/order/{id}", response_model=r_orderid)
def get_order_id(id: int, current_user: User = Depends(get_current_user)):
    return controller_order.get_order_id(id, current_user)
