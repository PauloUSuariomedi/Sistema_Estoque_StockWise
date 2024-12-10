from django.http import HttpRequest
from django.shortcuts import redirect


def redirect_view(request: HttpRequest):
    return redirect("admin:index")
