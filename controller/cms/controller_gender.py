from fastapi import status, HTTPException
from service.cms import service_gender

msgErr500 = HTTPException(
    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    detail="Server error.",
)


def c_gender(json):
    try:
        service_gender.s_create_gender(json)
        return {"detail": "Género criado.", "status": 201}
    except Exception as err:
        if err.errno == 1062:
            return {"detail": "Género já existe.", "status": 409}
        print("cms -> c_category ->", err)
        raise msgErr500
