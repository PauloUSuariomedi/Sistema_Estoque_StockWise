from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db import models


class User(AbstractUser):
    email = models.EmailField(verbose_name=_("E-mail"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email
