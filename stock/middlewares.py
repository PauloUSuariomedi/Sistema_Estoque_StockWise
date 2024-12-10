from typing import Any

from django.http import HttpRequest


class LoggerMiddlewares:
    def __init__(self, get_response) -> None:
        self.get_response = get_response

    def __call__(self, request: HttpRequest) -> Any:
        return self.get_response(request)
