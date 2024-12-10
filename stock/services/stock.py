from typing import Any
from stock.models import Product, Stock, Supplier


class StockService:
    def __init__(self, stock: Stock) -> None:
        self._stock = stock

    def entry(
        self,
        product: Product,
        quantity: int,
        supplier: Supplier,
    ):
        from stock.models import StockEntry

        StockEntry.objects.create(
            stock=self._stock,
            product=product,
            quantity=quantity,
            supplier=supplier,
        )

        self._stock.quantity += quantity
        self._stock.save(update_fields=("quantity",))

        if self._stock.quantity <= self._stock.max_quantity:
            self._dispatch_events(
                product.user,
                f"O estoque para o produto {product}, está acima do configurado",
            )

    def exit(
        self,
        product: Product,
        quantity: int,
        description: str,
    ):
        from stock.models import StockExit

        StockExit.objects.create(
            stock=self._stock,
            product=product,
            quantity=quantity,
            description=description,
        )
        self._stock.quantity -= quantity
        self._stock.save(update_fields=("quantity",))

        if self._stock.quantity <= self._stock.minimal_quantity:
            self._dispatch_events(
                product.user,
                f"O estoque para o produto {product}, está abaixo do configurado",
            )

    def _dispatch_events(self, user: Any, message: str):
        from stock.models import Notification
        from integrations.utils import notify

        notification = Notification.objects.create(
            destination=user,
            body=message,
        )

        notify(notification=notification)
