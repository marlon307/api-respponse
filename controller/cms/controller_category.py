from fastapi import status, HTTPException
from service.cms import service_category

msgErr500 = HTTPException(
    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    detail="Server error.",
)


def c_category(json):
    try:
        service_category.s_create_category(json)
        return {"detail": "Categoria criada.", "status": 201}
    except Exception as err:
        if err.errno == 1062:
            return {"detail": "Categoria já existe.", "status": 409}
        print("cms -> c_category ->", err)
        raise msgErr500
