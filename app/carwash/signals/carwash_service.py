###
# Libs
###
from django.db.models.signals import pre_save
from django.dispatch import receiver

from app.carwash.models.carwash_service import CarWashService


###
# Signals
###


@receiver(pre_save, sender=CarWashService)
def update_carwash_service_price(sender, instance, **kwargs):
    if instance.pk is None:
        instance.price = instance.service_type.price
    else:
        if instance.service_type != sender.objects.get(pk=instance.pk).service_type:
            instance.price = instance.service_type.price
