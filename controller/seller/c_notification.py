from service.seller import service_notification
from utility.handleErr import handlerErr


def seller_notification(data, request):
    try:
        service_notification.notification_seller(data, request)
        return {
            "detail": "Notificação.",
            "status": 200,
        }
    except Exception as err:
        raise handlerErr("seller -> c_notification -> %s" % err)
