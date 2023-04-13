from django.contrib import admin
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.utils.html import format_html

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


class BlockOffEntityInline(admin.TabularInline):
    model = BlockOffEntity
    extra = 0


class BrightnessConfigInline(admin.TabularInline):
    model = BrightnessConfig
    extra = 0


class LightConfigurationInline(admin.StackedInline):
    model = LightConfig
    extra = 0


class AreaInline(admin.StackedInline):
    model = Area
    extra = 0


class HouseAdmin(admin.ModelAdmin):
    inlines = [AreaInline]


class RoomInline(admin.StackedInline):
    model = Room
    extra = 0


class AreaAdmin(admin.ModelAdmin):
    inlines = [RoomInline]

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related("house")


class RoomAdmin(admin.ModelAdmin):
    readonly_fields = ("light_configuration_link",)

    def light_configuration_link(self, obj):
        if obj.lightconfig:
            url = reverse(
                "admin:inventory_lightconfig_change",
                args=[obj.lightconfig.id],
            )
            return format_html('<a href="{}">Edit Light Configuration</a>', url)
        return "No Light Configuration"

    light_configuration_link.short_description = "Light Configuration"

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related("lightconfig", "area")


class LightConfigurationAdmin(admin.ModelAdmin):
    inlines = [BlockOffEntityInline, BrightnessConfigInline]

    def save_model(self, request, obj, form, change):
        try:
            obj.clean()
            super().save_model(request, obj, form, change)
        except ValidationError as e:
            form.add_error(None, e)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related("room", "area")


admin.site.register(House, HouseAdmin)
admin.site.register(Device)
admin.site.register(DeviceType)
admin.site.register(Area, AreaAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(LightConfig, LightConfigurationAdmin)
admin.site.register(BlockOffEntity)
admin.site.register(BrightnessConfig)
