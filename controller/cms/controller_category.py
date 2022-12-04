from service.cms import service_category
from utility.handleErr import handlerErr, status, JSONResponse


def c_category(json):
    try:
        result = service_category.s_create_category(json)
        if result is True:
            return {"detail": "Categoria criada.", "status": 201}
        return JSONResponse(
            content={
                "datail": "Categoria já existe.",
                "status_code": status.HTTP_409_CONFLICT,
            },
            result=status.HTTP_409_CONFLICT,
        )
    except Exception as err:
        raise handlerErr("cms -> c_category -> %s" % err)
