from fastapi import APIRouter, File, Form, status, HTTPException
import json
from pydantic import ValidationError
from controller.seller import c_product
from middleware.m_auth import User, get_current_adm
from middleware.seller.m_product import m_create_product
from .models import Default

router = APIRouter(tags=["SELLER"])

format_str = {
    "categorys_id": 0,
    "gender_id": 0,
    "user_id": 0,
    "title": "Tilte",
    "subTitle": "subTitle",
    "warranty": 0,
    "details": "Details ...",
    "specifications": "Specifications ...",
    "list_qtd": [
        {
            "colors_id": 0,
            "sizes_id": 0,
            "quantity": 0,
            "price": 0,
            "discount": 0,
            "sku": "SKU",
        }
    ],
}

msgErr415 = HTTPException(
    status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
    detail="Server error.",
)


@router.post("/product", response_model=Default, status_code=201)
def create_product(
    file: list[bytes] = File(description="Multiple files as UploadFile"),
    data: str = Form(
        default=json.dumps(format_str),
        description="Copie as informaçoes do input e altere os valores mantendo o formato (JSON)",
    )
    # current_user: User = Depends(get_current_adm)
):
    try:
        n_data = m_create_product(**json.loads(data))
        # return {"detail": "ok", "status": 200}
        return c_product.product(n_data.dict(), file)
    except ValidationError as e:
        print("Route -> product: ", e.raw_errors)
        raise msgErr415


@router.get("/product")
def list_product():
    return c_product.list_product()


@router.get("/product/{id}")
def get_product_id(id: int):
    return c_product.get_product_id(id)
