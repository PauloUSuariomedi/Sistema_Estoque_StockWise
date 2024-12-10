from django.db import models
from django.utils.translation import gettext_lazy as _


class Email(models.Model):
    class Meta:
        verbose_name = _("E-mail")
        verbose_name_plural = _("E-mails")

    email = models.EmailField(
        verbose_name=_("E-mail"),
    )

    def __str__(self):
        return str(self.email)
