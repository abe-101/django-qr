import uuid

import segno
from django.db import models
from django.urls import reverse


class QRCode(models.Model):
    """
    Represents a QR code with associated metadata.

    This model stores information about QR codes, including their target URL,
    creation time, and last update time.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    target_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL for the QR code redirection view.

        Returns:
            str: The absolute URL for this QR code.

        """
        return reverse("django_qr:qr_redirect", kwargs={"pk": self.pk})

    @property
    def qrcode(self) -> segno.QRCode:
        """
        Generate a QR code for this instance.

        Returns:
            segno.QRCode: A QR code object representing the absolute URL
            of this instance.

        """
        return segno.make(self.get_absolute_url())
