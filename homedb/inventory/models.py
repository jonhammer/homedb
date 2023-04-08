from django.db import models


class House(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

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
        ('', 'Not specified'),
        ('zigbee', 'Zigbee'),
        ('zwave', 'Z-Wave'),
        ('ip', 'IP'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=255)
    device_type = models.ForeignKey(DeviceType, on_delete=models.CASCADE)
    protocol = models.CharField(max_length=10, choices=DEVICE_PROTOCOL_CHOICES, blank=True, default='')
    manufacturer = models.CharField(max_length=255, blank=True, default='')
    model = models.CharField(max_length=255, blank=True, default='')
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return self.name