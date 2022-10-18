from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from controller.user import controller_bag
from middleware.m_auth import User, get_current_user
from middleware.user.m_bag import add_bag, del_bag, up_bag, r_order
from ..user.models import Default, rListBag


router = APIRouter(tags=["USER"])


@router.post("/bag", response_model=Default, status_code=201)
def additembag(data: add_bag, current_user: User = Depends(get_current_user)):
    return controller_bag.c_add_bag(jsonable_encoder(data), current_user)


@router.get("/bag", response_model=rListBag)
def listbag(current_user: User = Depends(get_current_user)):
    return controller_bag.c_list_bag(current_user)


@router.patch("/bag", response_model=Default)
def updatequantity(data: up_bag, current_user: User = Depends(get_current_user)):
    return controller_bag.c_bag_update_quantity(jsonable_encoder(data), current_user)


@router.delete("/bag", response_model=Default)
def deleteitembag(data: del_bag, current_user: User = Depends(get_current_user)):
    return controller_bag.c_bag_delete(jsonable_encoder(data), current_user)


@router.post("/register_order", response_model=Default, status_code=201)
def registerorder(data: r_order, current_user: User = Depends(get_current_user)):
    return controller_bag.c_bag_register_order(jsonable_encoder(data), current_user)
