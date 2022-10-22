from fastapi import APIRouter, File, Form, status, HTTPException, Depends
import json
from pydantic import ValidationError
from controller.seller import c_product
from middleware.m_auth import User, get_current_adm
from middleware.seller.m_product import m_create_product
from .models import Default, ProductId, ListProduct, OptionProduct

router = APIRouter(tags=["SELLER"], dependencies=[])

format_str = {
    "categorys_id": 0,
    "gender_id": 0,
    "title": "Tilte",
    "subTitle": "subTitle",
    "warranty": 0,
    "details": "Details ...",
    "specifications": "Specifications ...",
    "list_qtd": [
        {
            "id": 0,
            "color": "#EXA",
            "sizes_id": [
                {
                    "id": 0,
                    "qunatity": 0,
                }
            ],
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
    ),
    current_user: User = Depends(get_current_adm),
):
    try:
        # validar informações do
        serialize_json = json.loads(data)
        serialize_json["id_user"] = current_user.id_user
        n_data = m_create_product(**serialize_json)
        return c_product.product(n_data.dict(), file)
    except ValidationError as e:
        print("Route -> product: ", e.raw_errors)
        raise msgErr415


@router.get("/product", response_model=ListProduct)
def list_product():
    return c_product.list_product()


@router.get("/product/{id}", response_model=ProductId)
def get_product_id(id: int):
    return c_product.get_product_id(id)


@router.get("/list_options")
def list_options():
    result = c_product.options()
    print(result)
    return result
