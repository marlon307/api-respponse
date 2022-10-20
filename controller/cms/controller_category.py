from service.cms import service_category
from utility.handleErr import handlerErr, status, HTTPException


def c_category(json):
    try:
        service_category.s_create_category(json)
        return {"detail": "Categoria criada.", "status": 201}
    except Exception as err:
        if err.errno == 1062:
            raise HTTPException(
                datail="Categoria já existe.",
                status_code=status.HTTP_409_CONFLICT,
            )
        raise handlerErr("cms -> c_category -> %s" % err)
