"""
API V1: Vehicle License Plate Views
"""
###
# Libs
###
from rest_framework import viewsets

from app.carwash.api.v1.serializers.vehicle_license_plate.default import DefaultVehicleLicensePlateSerializer
from app.carwash.models.vehicle_license_plate import VehicleLicensePlate


###
# Viewsets
###


class VehicleLicensePlateViewSet(viewsets.ModelViewSet):
    queryset = VehicleLicensePlate.objects.all().order_by('id')
    serializer_class = DefaultVehicleLicensePlateSerializer
