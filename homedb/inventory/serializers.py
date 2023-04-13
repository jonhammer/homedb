from rest_framework import serializers

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


class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = "__all__"


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = "__all__"


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"


class DeviceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceType
        fields = "__all__"


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = "__all__"


class LightConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = LightConfig
        fields = "__all__"


class BlockOffEntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlockOffEntity
        fields = "__all__"


class BrightnessConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrightnessConfig
        fields = "__all__"
