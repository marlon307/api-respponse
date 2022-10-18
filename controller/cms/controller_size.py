from fastapi import status, HTTPException
from service.cms import service_size

msgErr500 = HTTPException(
    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    detail="Server error.",
)


def c_size(json):
    try:
        service_size.s_create_size(json)
        return {"detail": "Tamanho criado.", "status": 201}
    except Exception as err:
        if err.errno == 1062:
            return {"detail": "Este tamnho já existe.", "status": 409}
        print("cms -> c_size ->", err)
        raise msgErr500
