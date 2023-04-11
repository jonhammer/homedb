from django.db import models


class House(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Area(models.Model):
    name = models.CharField(max_length=255)
    house = models.ForeignKey(House, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Room(models.Model):
    name = models.CharField(max_length=255)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class DeviceType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Device(models.Model):
    DEVICE_PROTOCOL_CHOICES = [
        ("", "Not specified"),
        ("zigbee", "Zigbee"),
        ("zwave", "Z-Wave"),
        ("ip", "IP"),
        ("other", "Other"),
    ]
    DEVICE_STATUS_CHOICES = [
        ("commissioned", "Commissioned"),
        ("installed", "Installed"),
        ("storage", "Storage"),
    ]

    name = models.CharField(max_length=255)
    device_type = models.ForeignKey(DeviceType, on_delete=models.CASCADE)
    protocol = models.CharField(
        max_length=32, choices=DEVICE_PROTOCOL_CHOICES, blank=True, default=""
    )
    manufacturer = models.CharField(max_length=255, blank=True, default="")
    model = models.CharField(max_length=255, blank=True, default="")
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    management_url = models.URLField(blank=True, default="")
    home_assistant_url = models.URLField(blank=True, default="")
    status = models.CharField(max_length=32, choices=DEVICE_STATUS_CHOICES)
    mac_address = models.CharField(max_length=255, blank=True, default="")

    def __str__(self):
        return self.name


class LightConfiguration(models.Model):
    area = models.OneToOneField(Area, on_delete=models.CASCADE, null=True, blank=True)
    room = models.OneToOneField(Room, on_delete=models.CASCADE, null=True, blank=True)
    timer = models.IntegerField()  # In minutes
    sun_elevation_cutoff = models.FloatField()
    before_time_cutoff = models.TimeField()
    after_time_cutoff = models.TimeField()
    lux_cutoff = models.FloatField()
    brightness = models.FloatField()

    def __str__(self):
        if self.area:
            return f"Light Configuration for Area: {self.area.name}"
        elif self.room:
            return f"Light Configuration for Room: {self.room.name}"
        else:
            return f"Unassociated Light Configuration (ID: {self.pk})"


class LightBlockingDevice(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    state = models.CharField(max_length=255)

    def __str__(self):
        return f"Light Blocking Device: {self.device.name} in Room: {self.room.name}"
