###
# Libs
###
from django.db import models
from django.utils.translation import gettext as _

from helpers.timestamp.models.timestamp import TimestampModel


###
# Model
###
class ServiceType(TimestampModel):
    name = models.CharField(
        max_length=30,
        unique=True,
        verbose_name=_('Service Type'),
    )
    price = models.FloatField(
        verbose_name=_('Price'),
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name=_('Is Active'),
    )
    description = models.TextField(
        verbose_name=_('Description'),
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Service Type')
        verbose_name_plural = _('Service Types')
