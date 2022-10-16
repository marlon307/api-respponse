from fastapi import APIRouter, Depends
from middleware.m_auth import User, get_current_user
from controller.user.controller_order import cOrders
from ..user.models import r_order, r_orderid

router = APIRouter(tags=["USER"])


@router.get("/order", response_model=r_order)
def get_orders(current_user: User = Depends(get_current_user)):
    return cOrders.c_get_orders(current_user)


@router.get("/order/{id}", response_model=r_orderid)
def get_order_id(id: int, current_user: User = Depends(get_current_user)):
    return cOrders.c_get_order_id(id, current_user)
