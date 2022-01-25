from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import AddressViewSet, GroupViewSet

router = DefaultRouter()
router.register("group", GroupViewSet)
router.register("address", AddressViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
