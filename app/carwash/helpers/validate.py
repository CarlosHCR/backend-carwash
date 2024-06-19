###
# Libs
###
from django.core.exceptions import ValidationError
from django.utils.timezone import now
from datetime import time


from app.carwash.models.carwash_service import CarWashService

###
# Helpers
###


def validate_service_date(attrs):
    service_date = attrs.get('service_date')

    if not service_date:
        raise ValidationError(
            'The service date is required.')

    start_time = time(7, 0)
    end_time = time(18, 0)

    if service_date <= now():
        raise ValidationError(
            'The date needs to be valid. The service must be scheduled for the future.')

    if service_date.time() < start_time or service_date.time() > end_time:
        raise ValidationError(
            'The service must be scheduled between 8:00 and 18:00.')

    if service_date.weekday() > 4:
        raise ValidationError(
            'The service must be scheduled between Monday and Friday.')

    existing_service = CarWashService.objects.filter(
        service_date=service_date).first()

    if existing_service:
        raise ValidationError(
            'The date is not available. Please choose another date and time.')
