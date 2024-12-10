from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    class Meta:
        verbose_name = _("Categoria")
        verbose_name_plural = _("Categorias")

    name = models.CharField(
        verbose_name=_("Nome"),
        max_length=150,
    )
    description = models.TextField(
        verbose_name=_("Descrição"),
        blank=True,
        null=True,
        default="",
    )

    def __str__(self) -> str:
        return str(self.name)
