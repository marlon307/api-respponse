from service.seller import service_notification
from utility.handleErr import handlerErr


def seller_notification(order_id, topic, id):
    try:
        nDict = {"order_id": order_id, "topic": topic, "id": id}
        service_notification.notification_seller(nDict)
        return {
            "detail": "Notificação.",
            "status": 200,
        }
    except Exception as err:
        raise handlerErr("seller -> c_notification -> %s" % err)
