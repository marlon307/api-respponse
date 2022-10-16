from fastapi import status, HTTPException
from service.cms.service_status import sStatus

msgErr500 = HTTPException(
    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    detail="Server error.",
)


class cStatus:
    def c_status(json):
        try:
            sStatus.s_create_status(json)
            return {"detail": "Status criado.", "status": 201}
        except Exception as err:
            if err.errno == 1062:
                return {"detail": "Este status já existe.", "status": 409}
            print("cms -> c_size ->", err)
            raise msgErr500
