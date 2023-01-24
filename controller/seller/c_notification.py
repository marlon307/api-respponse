from service.seller import service_notification
from utility.handleErr import handlerErr


def seller_notification(topic, id):
    try:
        nDict = {"topic": topic, "id": id}
        service_notification.notification_seller(nDict)
        return {
            "detail": "Notificação.",
            "status": 200,
        }
    except Exception as err:
        raise handlerErr("seller -> c_notification -> %s" % err)
