from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class Notification(models.Model):
    class Meta:
        verbose_name = _("Notificação")
        verbose_name_plural = _("Notificações")

    destination = models.ForeignKey(
        verbose_name=_("Destinatário"),
        to=settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="notifications",
        blank=True,
        null=True,
    )
    read = models.BooleanField(
        verbose_name=_("Lida"),
        blank=True,
        db_index=True,
    )
    body = models.TextField(
        verbose_name=_("Corpo"),
        blank=True,
        default="",
    )

    def __str__(self) -> str:
        return str(self.destination)
