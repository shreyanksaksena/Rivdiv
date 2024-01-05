# Defining the URL patterns
# App-level URL configurations

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InvoiceViewSet, InvoiceDetailViewSet

router = DefaultRouter()
router.register(r'invoices', InvoiceViewSet)
router.register(r'invoices/<int:pk>', InvoiceDetailViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
