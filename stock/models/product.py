from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from .base import BaseModel


class Product(BaseModel):
    class Meta:
        verbose_name = _("Produto")
        verbose_name_plural = _("Produtos")

    class ProductType(models.TextChoices):
        DIGITAL = "digital", _("Digital")
        PHYSICAL = "physical", _("Físico")

    user = models.ForeignKey(
        verbose_name=_("Usuário"),
        to=settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="products",
        blank=True,
        null=True,
    )
    name = models.CharField(
        verbose_name=_("Nome do produto"),
        max_length=255,
        db_index=True,
    )
    description = models.TextField(
        verbose_name=_("Descrição"),
        blank=True,
        null=True,
        default="",
    )
    base_price = models.DecimalField(
        verbose_name=_("Preço base"),
        max_digits=10,
        decimal_places=2,
    )
    categories = models.ManyToManyField(
        verbose_name=_("Categorias"),
        to="stock.Category",
        related_name="products",
    )

    def __str__(self):
        return f"{self.name}"
