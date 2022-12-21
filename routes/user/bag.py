from fastapi import APIRouter, BackgroundTasks, Depends
from controller.user import controller_bag
from middleware.m_auth import User, get_current_user
from middleware.user.m_bag import Carriers, add_bag, del_bag, up_bag, r_order
from ..user.models import Default, ListBag, RgOrder


router = APIRouter(tags=["USER"])


@router.post("/bag", response_model=Default, status_code=201)
def additembag(data: add_bag, current_user: User = Depends(get_current_user)):
    return controller_bag.c_add_bag(data.dict(), current_user)


@router.get("/bag", response_model=ListBag)
def listbag(current_user: User = Depends(get_current_user)):
    return controller_bag.c_list_bag(current_user)


@router.patch("/bag", response_model=Default)
def updatequantity(data: up_bag, current_user: User = Depends(get_current_user)):
    return controller_bag.c_bag_update_quantity(data.dict(), current_user)


@router.delete("/bag", response_model=Default)
def deleteitembag(data: del_bag, current_user: User = Depends(get_current_user)):
    return controller_bag.c_bag_delete(data.dict(), current_user)


@router.post("/register_order", response_model=RgOrder, status_code=201)
def registerorder(
    data: r_order, task: BackgroundTasks, current_user: User = Depends(get_current_user)
):
    return controller_bag.c_bag_register_order(data.dict(), current_user, task)


@router.post("/calc", status_code=200)
def registerorder(cep: Carriers, current_user: User = Depends(get_current_user)):
    return controller_bag.c_bag_calc_shipping(cep.dict(), current_user)
