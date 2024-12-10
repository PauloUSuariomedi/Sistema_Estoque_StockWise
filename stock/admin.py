"""
Admin configuration for the stock application.
This module contains the admin configurations for the stock application models,
including User, Product, Category, Stock, StockEntry, StockExit, Notification,
Supplier, and LogEntry.
Classes:
    UserAdmin: Custom admin interface for the User model.
    StockInlineAdmin: Inline admin interface for the Stock model.
    ProductAdmin: Custom admin interface for the Product model.
    CategoryAdmin: Admin interface for the Category model.
    ProductStockAdmin: Custom admin interface for the Stock model.
    StockEntryAdmin: Custom admin interface for the StockEntry model.
    StockExitAdmin: Custom admin interface for the StockExit model.
    NotificationAdmin: Admin interface for the Notification model.
    SupplierAdmin: Custom admin interface for the Supplier model.
    LogEntryAdmin: Custom admin interface for the LogEntry model.
Each class customizes the admin interface for its respective model, including
read-only fields, list displays, permissions, and custom save and delete
behaviors.
"""

from collections import OrderedDict
from typing import Any

from django.contrib import admin, messages
from django.contrib.admin.models import LogEntry
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from django.db.models import Model
from django.db.models.query import QuerySet
from django.forms import BaseModelFormSet, Form, ModelForm
from django.http import HttpRequest
from django.template.defaultfilters import floatformat
from django.utils.safestring import mark_safe
from unfold.admin import ModelAdmin, TabularInline

from stock import models

admin.site.unregister(Group)


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    """
    GroupAdmin class that inherits from BaseGroupAdmin and ModelAdmin.
    This class is used to customize the admin interface for the Group model.
    Currently, it does not add any additional functionality or customization.
    """


@admin.register(models.User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    """
    Custom admin class for managing user-related operations in the Django admin interface.

    Attributes:
        add_fieldsets (tuple): A tuple defining the layout for the user creation
        form in the admin interface.
            It includes the following fields:
            - username: The username of the user.
            - email: The email address of the user.
            - password1: The first password input for the user.
            - password2: The second password input for the user (for confirmation).
    """

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "email", "password1", "password2"),
            },
        ),
    )


# Uqp6F07KnTeGU2


class StockInlineAdmin(TabularInline):
    """
    StockInlineAdmin is a custom inline admin class for the Stock model.
    Attributes:
        model (models.Stock): The model associated with this inline admin.
        extra (int): The number of extra forms to display in the inline formset.
    Methods:
        has_change_permission(request: HttpRequest, obj: Any | None = ...) -> bool:
            Returns False to indicate that change permissions are not granted.
        has_add_permission(request: HttpRequest, obj: Any | None = ...) -> bool:
            Returns False to indicate that add permissions are not granted.
        has_delete_permission(request: HttpRequest, obj: Any | None = ...) -> bool:
            Returns False to indicate that delete permissions are not granted.
    """

    model = models.Stock
    extra = 0

    def has_change_permission(
        self, request: HttpRequest, obj: Any | None = ...
    ) -> bool:
        return False

    def has_delete_permission(
        self, request: HttpRequest, obj: Any | None = ...
    ) -> bool:
        return False


@admin.register(models.Product)
class ProductAdmin(ModelAdmin):
    """
    Admin interface for the Product model.
    Attributes:
        readonly_fields (tuple): Fields that are read-only in the admin interface.
        inlines (tuple): Inline admin classes to be displayed on the Product admin page.
    Methods:
        save_model(request, obj, form, change):
            Saves the Product instance. If the product does not have a user,
            assigns the current user.
            Ensures a Stock instance is created for the product if it does not already exist.
        delete_model(request, obj):
            Deletes the Product instance along with its related stock entries,
            stock exits, and stocks.
    """

    search_fields = ("name",)

    readonly_fields = ("code", "user")
    inlines = (StockInlineAdmin,)

    def save_model(
        self,
        request: HttpRequest,
        obj: models.Product,
        form: Form,
        change: Any,
    ) -> None:
        super().save_model(request, obj, form, change)

        obj.refresh_from_db()

        if not obj.user:
            obj.user = request.user
            obj.save(update_fields=("user",))

    def save_related(
        self,
        request: HttpRequest,
        form: ModelForm,
        formsets: BaseModelFormSet,
        change: bool,
    ) -> None:
        super().save_related(
            request,
            form,
            formsets,
            change,
        )
        # Verify if exists a stock for the product
        stock = form.instance.stocks.first()

        if not stock:
            stock, _ = models.Stock.objects.update_or_create(
                product=form.instance,
                defaults={
                    "quantity": 0,
                    "minimal_quantity": 1,
                    "max_quantity": 25,
                },
            )

        stock.refresh_from_db()

        if stock and stock.quantity > 0:
            stock_entry = models.StockEntry.objects.create(
                stock=stock,
                product=stock.product,
                supplier=stock.supplier,
                quantity=stock.quantity,
            )
            stock_entry.save()
            self.log_change(
                request,
                stock_entry,
                f"Foram adicionadas {stock_entry.quantity} unidades ao estoque",
            )

    def delete_model(self, request: HttpRequest, obj: Any) -> None:
        # Delete stock, entries and exits
        obj.stock_entries.all().delete()
        obj.stock_exits.all().delete()
        obj.stocks.all().delete()

        super().delete_model(request, obj)


@admin.register(models.Category)
class CategoryAdmin(ModelAdmin):
    """
    Admin interface for the Category model.
    Attributes:
        readonly_fields (tuple): Fields that are read-only in the admin interface.
    """

    list_display = ("name",)


@admin.register(models.Stock)
class ProductStockAdmin(ModelAdmin):
    """
    Admin interface for managing product stock.
    Attributes:
        readonly_fields (tuple): Fields that are read-only in the admin interface.
        list_display (tuple): Fields to display in the list view of the admin interface.
    Methods:
        stock_state(obj: Model) -> str:
            Returns the stock state as an HTML formatted string based on the quantity.
        save_model(request: HttpRequest, obj: models.Stock, form: Form, change: Any) -> None:
            Overrides the save_model method to handle stock entry and exit logging,
            and to send notifications if the stock quantity is below the minimum
            or above the maximum.
    """

    readonly_fields = ("code",)

    list_display = (
        "product",
        "quantity",
        "total_value_in_stock",
        "stock_state",
    )

    search_fields = ("product__name",)

    @admin.display(description="Estado do estoque")
    def stock_state(self, obj: Model) -> str:
        """
        Determines the stock state of a given object based on its quantity.
        Args:
            obj (Model): The object containing stock information.
        Returns:
            str: An HTML string representing the stock state with appropriate styling.
                - "Baixo" (Low) if the quantity is less than the minimal quantity.
                - "Alto" (High) if the quantity is greater than the maximum quantity.
                - "Normal" if the quantity is within the acceptable range.
        """
        if obj.quantity < obj.minimal_quantity:
            text = mark_safe(
                "<span class='inline-flex items-center rounded-md bg-red-50 px-2 py-1 text-xs font-medium text-red-700 ring-1 ring-inset ring-red-600/10'>Baixo</span>"
            )
            return text
        if obj.quantity > obj.max_quantity:
            text = mark_safe(
                "<span class='inline-flex items-center rounded-md bg-red-50 px-2 py-1 text-xs font-medium text-red-700 ring-1 ring-inset ring-red-600/10'>Alto</span>"
            )
            return text

        text = mark_safe(
            "<span class='inline-flex items-center rounded-md bg-green-50 px-2 py-1 text-xs font-medium text-green-700 ring-1 ring-inset ring-green-600/20'>Normal</span>"
        )

        return text

    @admin.display(description="Valor total em estoque")
    def total_value_in_stock(self, obj: Model) -> str:
        text = mark_safe(
            f"R$ {floatformat(obj.quantity * obj.product.base_price, '2g')}"
        )
        return text

    def save_model(
        self,
        request: HttpRequest,
        obj: models.Stock,
        form: Form,
        change: Any,
    ) -> None:
        from stock.models import Notification

        if change:
            old_stock = models.Stock.objects.get(pk=obj.pk)

            if obj.quantity != old_stock.quantity:
                if obj.quantity < old_stock.quantity:
                    stock_exit = models.StockExit.objects.create(
                        stock=obj,
                        product=obj.product,
                        quantity=old_stock.quantity - obj.quantity,
                    )
                    stock_exit.save()
                    self.log_change(
                        request,
                        stock_exit,
                        f"Foram retiradas {stock_exit.quantity} unidades do estoque",
                    )

                if obj.quantity > old_stock.quantity:
                    stock_entry = models.StockEntry.objects.create(
                        stock=obj,
                        product=obj.product,
                        supplier=obj.supplier,
                        quantity=obj.quantity - old_stock.quantity,
                    )
                    stock_entry.save()
                    self.log_change(
                        request,
                        stock_entry,
                        f"Foram adicionadas {stock_entry.quantity} unidades ao estoque",
                    )

        super().save_model(request, obj, form, change)

        if obj.quantity < obj.minimal_quantity:
            notification = Notification.objects.create(
                destination=obj.product.user,
                body=f"A quantidade do produto {obj.product} está abaixo da quantidade mínima!",
                read=False,
            )
            messages.warning(request=request, message=notification.body)

        if obj.quantity > obj.max_quantity:
            notification = Notification.objects.create(
                destination=obj.product.user,
                body=f"A quantidade do produto {obj.product} está acima da quantidade máxima!",
                read=False,
            )
            messages.warning(request=request, message=notification.body)


@admin.register(models.StockEntry)
class StockEntryAdmin(ModelAdmin):
    list_display = (
        "code",
        "product",
        "stock",
        "quantity",
        "created_at",
    )
    readonly_fields = (
        "code",
        "stock",
    )

    def has_change_permission(
        self, request: HttpRequest, obj: Any | None = ...
    ) -> bool:
        if request.user.is_superuser:
            return True
        return False

    def get_actions(self, request: HttpRequest) -> OrderedDict[Any, Any]:
        if request.user.is_superuser:
            return super().get_actions(request)
        return {}

    def save_model(
        self,
        request: HttpRequest,
        obj: Model,
        form: Form,
        change: Any,
    ) -> None:
        from stock.models import Notification

        # Before save the stock entry, set correct stock to change quantity
        obj.stock = obj.product.stocks.first()

        super().save_model(request, obj, form, change)
        obj.refresh_from_db()

        obj.stock.quantity += obj.quantity
        obj.stock.save(update_fields=("quantity",))

        self.log_change(
            request,
            obj,
            f"Foram adicionadas {obj.quantity} unidades ao estoque",
        )

        if obj.stock.quantity > obj.stock.max_quantity:
            notification = Notification.objects.create(
                destination=obj.product.user,
                body=f'A quantidade do produto "{obj.product}" está acima da quantidade máxima!',
                read=False,
            )
            messages.warning(request=request, message=notification.body)


@admin.register(models.StockExit)
class StockExitAdmin(ModelAdmin):
    list_display = (
        "code",
        "product",
        "stock",
        "quantity",
        "created_at",
    )

    readonly_fields = (
        "code",
        "stock",
    )

    def has_change_permission(
        self, request: HttpRequest, obj: Any | None = ...
    ) -> bool:
        if request.user.is_superuser:
            return True
        return False

    def get_actions(self, request: HttpRequest) -> OrderedDict[Any, Any]:
        if request.user.is_superuser:
            return super().get_actions(request)
        return {}

    def save_model(
        self,
        request: HttpRequest,
        obj: Model,
        form: Form,
        change: Any,
    ) -> None:
        from stock.models import Notification

        # Before save the stock entry, set correct stock to change quantity
        obj.stock = obj.product.stocks.first()

        super().save_model(request, obj, form, change)

        obj.stock.quantity -= obj.quantity
        obj.stock.save(update_fields=("quantity",))
        self.log_change(
            request,
            obj,
            f"Foram retiradas {obj.quantity} unidades do estoque",
        )

        if obj.stock.quantity < obj.stock.minimal_quantity:
            notification = Notification.objects.create(
                destination=obj.product.user,
                body=f'A quantidade do produto "{obj.product}" está abaixo da quantidade mínima!',
                read=False,
            )
            messages.warning(request=request, message=notification.body)


@admin.register(models.Notification)
class NotificationAdmin(ModelAdmin):
    pass


@admin.register(models.Supplier)
class SupplierAdmin(ModelAdmin):
    list_display = (
        "code",
        "name",
    )
    readonly_fields = ("code",)


@admin.register(LogEntry)
class LogEntryAdmin(ModelAdmin):
    list_display = (
        "user",
        "custom_repr",
        "change_message",
        "content_type",
        "action_flag",
        "action_time",
    )
    list_filter = ("action_flag",)

    @admin.display(description="Produto")
    def custom_repr(self, obj: Model) -> str:
        return obj.object_repr

    def has_add_permission(self, request: HttpRequest) -> bool:
        if request.user.is_superuser:
            return True
        return False

    def get_queryset(self, request: HttpRequest) -> QuerySet:
        queryset = super().get_queryset(request)
        return queryset.filter(
            content_type__model__in=(
                "product",
                "stockentry",
                "stockexit",
            ),
            change_message__contains="Foram",
        )

    def has_change_permission(
        self, request: HttpRequest, obj: Any | None = ...
    ) -> bool:
        if request.user.is_superuser:
            return True
        return False

    def has_delete_permission(
        self, request: HttpRequest, obj: Any | None = ...
    ) -> bool:
        if request.user.is_superuser:
            return True
        return False
