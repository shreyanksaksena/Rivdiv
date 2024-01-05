# Including the invoices app URLs
# Project-level URL configurations

from django.urls import path, include

urlpatterns = [
    path('', include('invoices.urls')),
]
