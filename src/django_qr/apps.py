from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class QrAppConfig(AppConfig):
    """App config for Django QR."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "django_qr"
    verbose_name = _("qr")
