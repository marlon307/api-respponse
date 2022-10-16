from fastapi import status, HTTPException
from service.cms.service_gender import sGender

msgErr500 = HTTPException(
    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    detail="Server error.",
)


class cGender:
    def c_gender(json):
        try:
            sGender.s_create_gender(json)
            return {"detail": "Género criado.", "status": 201}
        except Exception as err:
            if err.errno == 1062:
                return {"detail": "Género já existe.", "status": 409}
            print("cms -> c_category ->", err)
            raise msgErr500
