from service.cms import service_status
from utility.handleErr import handlerErr, status, HTTPException


def c_status(json):
    try:
        service_status.s_create_status(json)
        return {"detail": "Status criado.", "status": 201}
    except Exception as err:
        if err.errno == 1062:
            raise HTTPException(
                datail="Status já existe.",
                status_code=status.HTTP_409_CONFLICT,
            )
        raise handlerErr("cms -> c_size -> %s" % err)
