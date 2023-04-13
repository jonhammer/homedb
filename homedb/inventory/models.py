from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class House(models.Model):
    """
    Represents a house with a name.
    """

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Area(models.Model):
    """
    Represents an area within a house, with a name and a reference to the house it belongs to.
    """

    name = models.CharField(max_length=255)
    house = models.ForeignKey(House, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Room(models.Model):
    """
    Represents a room within an area, with a name and a reference to the area it belongs to.
    """

    name = models.CharField(max_length=255)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class DeviceType(models.Model):
    """
    Represents a type of device, with a name.
    """

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Device(models.Model):
    """
    Represents a device in a room, with a name, device type, protocol, manufacturer, model, room,
    management URL, home assistant URL, status, and MAC address.
    """

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


class LightConfig(models.Model):
    """
    Represents a light configuration for either an area or a room, with timer, sun elevation,
    time cutoffs, and lux cutoff. The configuration must be associated with either an area or
    a room, but not both.
    """

    area = models.OneToOneField(Area, on_delete=models.CASCADE, null=True, blank=True)
    room = models.OneToOneField(Room, on_delete=models.CASCADE, null=True, blank=True)
    timer = models.IntegerField(null=True, blank=True)  # In minutes
    sun_elevation_below_cutoff = models.IntegerField(blank=True, null=True)
    sun_elevation_above_cutoff = models.IntegerField(blank=True, null=True)
    before_time_cutoff = models.TimeField(blank=True, null=True)
    after_time_cutoff = models.TimeField(blank=True, null=True)
    lux_cutoff = models.IntegerField(blank=True, null=True)

    def __str__(self):
        if self.area:
            return f"{self.area.name}"
        elif self.room:
            return f"{self.room.name}"
        else:
            return "Unnamed Light Configuration"

    def clean(self):
        if self.area and self.room:
            raise ValidationError(
                "Light Configuration cannot be associated with both an Area and a Room."
            )
        if not self.area and not self.room:
            raise ValidationError(
                "Light Configuration must be associated with either an Area or a Room."
            )

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)


class BlockOffEntity(models.Model):
    """
    Represents a block off entity associated with a light configuration. It has an entity name
    and a block state, which by default is set to "on".
    """

    light_config = models.ForeignKey(LightConfig, on_delete=models.CASCADE)
    entity_name = models.CharField(max_length=255)
    block_state = models.CharField(max_length=255, blank=True, default="on")

    def __str__(self):
        return f"{self.light_config}: {self.entity_name}"

    class Meta:
        verbose_name_plural = "Block Off Entities"


class BrightnessConfig(models.Model):
    """
    Represents a brightness configuration associated with a light configuration. It has a
    brightness value (0-255), and a start time to apply the configuration.
    """

    light_config = models.ForeignKey(LightConfig, on_delete=models.CASCADE)
    brightness = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(255)]
    )
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.light_config}: {self.brightness} at {self.start_time}"

    def save(self, *args, **kwargs):
        # Ensure start time is before end time
        if self.start_time >= self.end_time:
            raise ValidationError("Start time must be before end time.")

        # Check for overlapping time periods
        overlapping_configs = BrightnessConfig.objects.filter(
            light_config=self.light_config,
            start_time__lt=self.end_time,
            end_time__gt=self.start_time,
        )

        # Exclude the current instance from the queryset if it's being updated
        if self.pk:
            overlapping_configs = overlapping_configs.exclude(pk=self.pk)

        if overlapping_configs.exists():
            raise ValidationError(
                "Overlapping time period with an existing BrightnessConfig for the same light_config."
            )

        super().save(*args, **kwargs)
