from django.db import models
from django.utils.translation import gettext_lazy as _

from .base import BaseModel


class Stock(BaseModel):
    class Meta:
        verbose_name = _("Estoque")
        verbose_name_plural = _("Estoques")

    product = models.ForeignKey(
        verbose_name=_("Produto"),
        to="stock.Product",
        on_delete=models.CASCADE,
        related_name="stocks",
        blank=True,
        null=True,
    )
    supplier = models.ForeignKey(
        verbose_name=_("Fornecedor"),
        to="stock.Supplier",
        on_delete=models.CASCADE,
        related_name="stocks",
        null=True,
    )
    quantity = models.PositiveIntegerField(
        verbose_name=_("Quantidade"),
        blank=True,
        null=True,
        default=0,
    )
    minimal_quantity = models.PositiveIntegerField(
        verbose_name=_("Quantidade minima"),
        blank=True,
        null=True,
        default=0,
    )
    max_quantity = models.PositiveIntegerField(
        verbose_name=_("Quantidade máxima"),
        blank=True,
        null=True,
        default=0,
    )

    def __str__(self):
        return str(self.product)


class StockEntry(BaseModel):
    class Meta:
        verbose_name = _("Entrada")
        verbose_name_plural = _("Entradas")

    stock = models.ForeignKey(
        verbose_name=_("Estoque"),
        to="stock.Stock",
        on_delete=models.CASCADE,
        related_name="stock_entries",
        blank=True,
        null=True,
    )
    product = models.ForeignKey(
        verbose_name=_("Produto"),
        to="stock.Product",
        on_delete=models.CASCADE,
        related_name="stock_entries",
        blank=True,
        null=True,
    )
    supplier = models.ForeignKey(
        verbose_name=_("Fornecedor"),
        to="stock.Supplier",
        on_delete=models.CASCADE,
        related_name="stock_entries",
        blank=True,
        null=True,
    )
    quantity = models.PositiveIntegerField(
        verbose_name=_("Quantidade"),
    )

    def __str__(self):
        return f"{self.product}"


class StockExit(BaseModel):
    class Meta:
        verbose_name = _("Saída")
        verbose_name_plural = _("Saídas")

    stock = models.ForeignKey(
        verbose_name=_("Estoque"),
        to="stock.Stock",
        on_delete=models.CASCADE,
        related_name="stock_exits",
        blank=True,
        null=True,
    )
    product = models.ForeignKey(
        verbose_name=_("Produto"),
        to="stock.Product",
        on_delete=models.CASCADE,
        related_name="stock_exits",
        blank=True,
        null=True,
    )
    quantity = models.PositiveIntegerField(
        verbose_name=_("Quantidade"),
    )

    def __str__(self):
        return f"{self.product}"
