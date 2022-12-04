from service.cms import service_size
from utility.handleErr import handlerErr, status, HTTPException


def c_size(json):
    try:
        service_size.s_create_size(json)
        return {"detail": "Tamanho criado.", "status": 201}
    except Exception as err:
        if err.errno == 1062:
            raise HTTPException(
                datail="Tamanho já existe.",
                status_code=status.HTTP_409_CONFLICT,
            )
        raise handlerErr("cms -> c_size -> %s" % err)
