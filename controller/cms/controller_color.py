from service.cms import service_color
from utility.handleErr import handlerErr,status,HTTPException


def c_color(json):
    try:
        service_color.s_create_color(json)
        return {"detail": "Cor criada.", "status": 201}
    except Exception as err:
        if err.errno == 1062:
            raise HTTPException(
                datail="Cor já existe.",
                status_code=status.HTTP_409_CONFLICT,
            )
        raise handlerErr("cms -> c_color -> %s" % err)
