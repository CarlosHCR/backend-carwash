###
# Libs
###
from django.db import models
from django.utils.translation import gettext as _

from app.accounts.models.user import User
from app.carwash.constants import AppointmentStatusMixin
from app.carwash.models.service_type import ServiceType
from app.carwash.models.vehicle_license_plate import VehicleLicensePlate
from helpers.timestamp.models.timestamp import TimestampModel


###
# Model
###
class CarWashService(TimestampModel):
    registered_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_('Registered by'),
    )
    vehicle_license_plate = models.ForeignKey(
        VehicleLicensePlate,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_('Vehicle License Plate'),
    )
    service_type = models.ForeignKey(
        ServiceType,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_('Service Type'),
    )
    service_date = models.DateTimeField(
        verbose_name=_('Service Date'),
    )
    status = models.CharField(
        max_length=20,
        choices=AppointmentStatusMixin.APPOINTMENT_CHOICES,
        default=AppointmentStatusMixin.SCHEDULED,
        verbose_name=_('Status'),
    )
    notes = models.TextField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name=_('Notes'),
    )
    price = models.FloatField(
        verbose_name=_('Price'),
    )

    class Meta:
        verbose_name = _('Car Wash Service')
        verbose_name_plural = _('Car Washes Services')
        indexes = [
            models.Index(fields=['service_date',]),
        ]
