from service.cms import service_carrier
from utility.handleErr import handlerErr


def c_refresh_carries():
    try:
        service_carrier.s_refresh_carries()
        return {
            "detail": "Transportadoras atualizada.",
            "status": 201,
        }
    except Exception as err:
        raise handlerErr("bag -> c_refresh_carries -> %s" % err)
