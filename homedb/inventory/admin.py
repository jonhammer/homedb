from django.contrib import admin

from .models import Area, Device, DeviceType, House, LightConfiguration, Room

admin.site.register(Area)
admin.site.register(Device)
admin.site.register(DeviceType)
admin.site.register(House)
admin.site.register(Room)
admin.site.register(LightConfiguration)
