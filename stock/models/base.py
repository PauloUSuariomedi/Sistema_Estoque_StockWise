from django.db import models
from django.utils.translation import gettext_lazy as _

from core.utils import random_code


class BaseModel(models.Model):
    class Meta:
        abstract = True

    code = models.CharField(
        verbose_name=_("Código"),
        max_length=25,
        db_index=True,
        default=random_code,
    )
    created_at = models.DateTimeField(
        verbose_name=_("Criado em"),
        db_index=True,
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name=_("Atualizado em"),
        auto_now=True,
    )
