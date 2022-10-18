from fastapi import status, HTTPException
from service.cms import service_color

msgErr500 = HTTPException(
    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    detail="Server error.",
)


def c_color(json):
    try:
        service_color.s_create_color(json)
        return {"detail": "Cor criada.", "status": 201}
    except Exception as err:
        if err.errno == 1062:
            return {"detail": "Esta cor já existe.", "status": 409}
        print("cms -> c_color ->", err)
        raise msgErr500
