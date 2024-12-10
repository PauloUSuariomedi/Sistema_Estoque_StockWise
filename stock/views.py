from django.http import HttpRequest, HttpResponse, JsonResponse


def register(request: HttpRequest):
    user = request.user
    return JsonResponse(
        {
            "channel": user.pk,
        }
    )


def stream(request: HttpRequest):
    from django_eventstream import send_event

    user = request.user

    send_event(str(user.pk), "message", {"text": "hello world"})
    return HttpResponse("Ok")
