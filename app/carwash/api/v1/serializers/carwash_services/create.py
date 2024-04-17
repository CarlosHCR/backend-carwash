"""
API V1: CarWash Service Default Serializers
"""
###
# Libs
###
from django.core.exceptions import ValidationError
from django.utils.timezone import now
from rest_framework import serializers

from app.accounts.constants import UserRolesMixin
from app.carwash.api.v1.serializers.service_type.default import DefaultServiceTypeSerializer
from app.carwash.api.v1.serializers.vehicle_license_plate.default import DefaultVehicleLicensePlateSerializer
from app.carwash.models.carwash_services import CarWashService
from app.carwash.models.service_type import ServiceType
from app.carwash.models.vehicle_license_plate import VehicleLicensePlate



###
# Serializers
###


class CreateCarWashServiceSerializer(serializers.ModelSerializer):
    license_plate_number = serializers.CharField(
        write_only=True)
    service_type = serializers.PrimaryKeyRelatedField(
        queryset=ServiceType.objects.all(), required=True)

    def validate(self, attrs):
        if 'license_plate_number' in attrs:
            license_plate_number = attrs.pop('license_plate_number')
            if license_plate_number:
                vehicle_license_plate, created = VehicleLicensePlate.objects.get_or_create(
                    number=license_plate_number)
                attrs['vehicle_license_plate'] = vehicle_license_plate

        if self.context['request'].user.role == UserRolesMixin.CLIENT:

            service_date = attrs.get('service_date')
            if service_date <= now():
                raise ValidationError(
                    'The date needs to be valid. The service must be scheduled for the future.')

        return super().validate(attrs)

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['vehicle_license_plate'] = DefaultVehicleLicensePlateSerializer(
            instance.vehicle_license_plate).data
        ret['service_type'] = DefaultServiceTypeSerializer(
            instance.service_type).data
        return ret

    class Meta:
        model = CarWashService
        fields = [
            'id', 'vehicle_license_plate', 'service_type',
            'service_date', 'status', 'notes', 'created_at',
            'license_plate_number', 'registered_by', 'price'
        ]
        extra_kwargs = {
            'vehicle_license_plate': {'read_only': True},
            'status': {'read_only': True},
            'price': {'read_only': True},
        }
