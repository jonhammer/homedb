from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .viewsets import (
    AreaViewSet,
    BlockOffEntityViewSet,
    BrightnessConfigViewSet,
    DeviceTypeViewSet,
    DeviceViewSet,
    HouseViewSet,
    LightConfigViewSet,
    RoomViewSet,
)

router = DefaultRouter()
router.register(r"houses", HouseViewSet)
router.register(r"areas", AreaViewSet)
router.register(r"rooms", RoomViewSet)
router.register(r"device-types", DeviceTypeViewSet)
router.register(r"devices", DeviceViewSet)
router.register(r"light-configs", LightConfigViewSet)
router.register(r"block-off-entities", BlockOffEntityViewSet)
router.register(r"brightness-configs", BrightnessConfigViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
