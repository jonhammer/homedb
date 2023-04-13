from rest_framework import viewsets

from .models import (
    Area,
    BlockOffEntity,
    BrightnessConfig,
    Device,
    DeviceType,
    House,
    LightConfig,
    Room,
)
from .serializers import (
    AreaSerializer,
    BlockOffEntitySerializer,
    BrightnessConfigSerializer,
    DeviceSerializer,
    DeviceTypeSerializer,
    HouseSerializer,
    LightConfigSerializer,
    RoomSerializer,
)


class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer


class AreaViewSet(viewsets.ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class DeviceTypeViewSet(viewsets.ModelViewSet):
    queryset = DeviceType.objects.all()
    serializer_class = DeviceTypeSerializer


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class LightConfigViewSet(viewsets.ModelViewSet):
    queryset = LightConfig.objects.all()
    serializer_class = LightConfigSerializer


class BlockOffEntityViewSet(viewsets.ModelViewSet):
    queryset = BlockOffEntity.objects.all()
    serializer_class = BlockOffEntitySerializer


class BrightnessConfigViewSet(viewsets.ModelViewSet):
    queryset = BrightnessConfig.objects.all()
    serializer_class = BrightnessConfigSerializer
