from django.urls import path

from .views import stream, register

urlpatterns = [
    path("channel/register/", register, name="register-channel"),
    path("sse/", stream, name="sse"),
]
