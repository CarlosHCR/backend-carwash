"""
API V1: Vehicle License Plate Default Serializers
"""
###
# Libs
###
from rest_framework import serializers

from app.carwash.models.vehicle_license_plate import VehicleLicensePlate


###
# Serializers
###


class DefaultVehicleLicensePlateSerializer(serializers.ModelSerializer):

    def to_internal_value(self, data):
        if hasattr(data, 'copy'):
            data = data.copy()

        if 'number' in data:
            data['number'] = data['number'].upper()

        return super(DefaultVehicleLicensePlateSerializer, self).to_internal_value(data)

    class Meta:
        model = VehicleLicensePlate
        fields = '__all__'
