"""
API V1: CarWash Service Default Serializers
"""
###
# Libs
###
from rest_framework import serializers

from app.carwash.api.v1.serializers.service_type.default import DefaultServiceTypeSerializer
from app.carwash.api.v1.serializers.vehicle_license_plate.default import DefaultVehicleLicensePlateSerializer
from app.carwash.models.carwash_service import CarWashService


###
# Serializers
###


class DefaultCarWashServiceSerializer(serializers.ModelSerializer):

    vehicle_license_plate = DefaultVehicleLicensePlateSerializer()
    service_type = DefaultServiceTypeSerializer()

    class Meta:
        model = CarWashService
        fields = '__all__'
