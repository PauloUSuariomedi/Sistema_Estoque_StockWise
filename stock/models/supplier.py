from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from .base import BaseModel


class Supplier(BaseModel):
    class Meta:
        verbose_name = _("Fornecedor")
        verbose_name_plural = _("Fornecedores")

    user = models.ForeignKey(
        verbose_name=_("Usuário"),
        to=settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="suppliers",
        blank=True,
        null=True,
    )
    name = models.CharField(
        verbose_name=_("Nome"),
        max_length=100,
    )

    def __str__(self):
        return str(self.name)
