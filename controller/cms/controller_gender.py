from service.cms import service_gender
from utility.handleErr import handlerErr, HTTPException, status


def c_gender(json):
    try:
        service_gender.s_create_gender(json)
        return {"detail": "Género criado.", "status": 201}
    except Exception as err:
        if err.errno == 1062:
            raise HTTPException(
                datail="Género já existe.",
                status_code=status.HTTP_409_CONFLICT,
            )
        raise handlerErr("cms -> c_category -> %s" % err)
