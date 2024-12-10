from stock.models import Notification


def notify(notification: Notification):
    from django_eventstream import send_event

    user = notification.destination
    message = notification.body

    send_event(str(user.pk), "message", {"text": message})

    notification.read = True
    notification.save(update_fields=("read",))
