###
# Libs
###
from django.db import models
from django.utils.translation import gettext as _
from django.core.validators import MinLengthValidator

from helpers.timestamp.models.timestamp import TimestampModel


###
# Model
###
class VehicleLicensePlate(TimestampModel):
    number = models.CharField(
        max_length=7,
        unique=True,
        verbose_name=_('Vehicle License Plate'),
        validators=[MinLengthValidator(7)],
    )

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = _('Vehicle License Plate')
        verbose_name_plural = _('Vehicle License Plates')
