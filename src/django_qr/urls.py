from django.urls import path

from .views import QRRedirectView

app_name = "django_qr"

urlpatterns = [
    path("<uuid:pk>/", QRRedirectView.as_view(), name="qr_redirect"),
]
