from fastapi import APIRouter, Depends
from middleware.m_auth import User, get_current_user
from middleware.user.m_address import m_addAddress, m_delAddress
from controller.user import controller_address
from ..user.models import Default, ListAdd, AddAddress


router = APIRouter(tags=["USER"])


@router.post("/address", response_model=AddAddress, status_code=201)
def addaddress(
    form: m_addAddress = Depends(m_addAddress.form_address),
    current_user: User = Depends(get_current_user),
):
    return controller_address.add_address(form.dict(), current_user)


@router.get("/address", response_model=ListAdd)
def getaddress(current_user: User = Depends(get_current_user)):
    return controller_address.get_address(current_user)


@router.delete("/address", response_model=Default)
def deleteaddress(data: m_delAddress, current_user: User = Depends(get_current_user)):
    return controller_address.delete_address(data.dict(), current_user.id_user)
