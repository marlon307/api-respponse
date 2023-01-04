import json
from fastapi import Form
from pydantic import BaseModel, HttpUrl, validator

format_str = (
    [
        {
            "id": 0,
            "color": "#EXA",
            "sizes": [
                {
                    "id": 0,
                    "quantity": 0,
                }
            ],
            "price": 0,
            "discount": 0,
            "sku": "SKU",
            "width": 0,
            "height": 0,
            "length": 0,
            "weight": 0,
        }
    ],
)


class OptionSizes(BaseModel):
    id: int
    quantity: int


class Options(BaseModel):
    id: int
    color: str
    price: float
    discount: float
    sku: str
    sizes: list[OptionSizes]
    width: float
    height: float
    length: float
    weight: float


class OptionTypeProduct(BaseModel):
    options: list[Options]


class CreateProduct(BaseModel):
    categorys_id: int
    title: str
    warranty: int
    gender_id: int
    details: str
    specifications: str
    list_qtd: str

    @validator("list_qtd")
    def convert_json_options(cls, v):
        data = json.loads(v)
        OptionTypeProduct(options=data)
        return data

    @classmethod
    def fields_product(
        cls,
        list_qtd: str = Form(
            default=str(format_str[0]),
            description="* Copie as informaçoes do input e altere os valores mantendo o formato (STRING/JSON)",
        ),
        categorys_id: int = Form(),
        title: str = Form(),
        warranty: int = Form(),
        gender_id: int = Form(),
        details: str = Form(),
        specifications: str = Form(),
    ):
        return cls(
            categorys_id=categorys_id,
            title=title,
            warranty=warranty,
            gender_id=gender_id,
            details=details,
            specifications=specifications,
            list_qtd=list_qtd,
        )


class ListImage(BaseModel):
    imgid: int
    urlImg: str
    option_id: int


class ListOption(BaseModel):
    idc: int
    color: str
    price: float
    discount: int
    colorName: str
    option_id: int
    sizes: dict
    images: list[ListImage]


class Product(BaseModel):
    id: int
    title: str
    details: str
    specifications: str
    category_name: str
    list_options: list[ListOption]


class ProductId(BaseModel):
    product: Product
    detail: str
    status: int


# List
class ListProdColor(BaseModel):
    id: int
    color: str
    price: float
    discount: int
    url_image: str
    color_name: str


class MinInfoProductList(BaseModel):
    id: int
    title: str
    category_name: str
    color_list: list[ListProdColor]


class CategoryPage(BaseModel):
    detail: str
    status: int
    products_ctg: list[MinInfoProductList]


class CategoryHome(BaseModel):
    id: int
    path: str
    color: str
    category_name: str
    sub_title: str
    url_image: HttpUrl


class Slides(BaseModel):
    id: int
    url_image: str
    title: str
    background: str
    description: str


class ListProduct(BaseModel):
    slides: list[Slides]
    list_products: list[MinInfoProductList] | dict
    categorys: list[CategoryHome] | dict
    detail: str
    status: int


# List Options
class Color(BaseModel):
    id: int
    color: str
    color_name: str


class Category(BaseModel):
    id: int
    color: str
    sub_title: str
    url_image: str
    category_name: str


class Gender(BaseModel):
    id: int
    gender: str
    gender_name: str


class Size(BaseModel):
    id: int
    size: str


class OptionList(BaseModel):
    list_colors: list[Color]
    list_ctg: list[Category]
    list_gender: list[Gender]
    list_sizes: list[Size]


class OptionProduct(BaseModel):
    option_list: OptionList
    detail: str
    status: int
