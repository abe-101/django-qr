from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.views import View

from .models import QRCode


class QRRedirectView(View):
    """View for redirecting to the target URL associated with a QR code."""

    def get(self, request: HttpRequest, pk: str) -> HttpResponseRedirect:
        """
        Handle GET requests for QR code redirection.

        Args:
            request (HttpRequest): The HTTP request object.
            pk (str): The primary key (UUID) of the QRCode instance.

        Returns:
            HttpResponseRedirect: A redirect response to the target URL.

        """
        qr_code = get_object_or_404(QRCode, pk=pk)
        return redirect(qr_code.target_url)
