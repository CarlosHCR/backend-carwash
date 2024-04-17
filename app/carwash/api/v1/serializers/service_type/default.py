"""
API V1: Service Type Default Serializers
"""
###
# Libs
###
from rest_framework import serializers

from app.carwash.models.service_type import ServiceType


###
# Serializers
###


class DefaultServiceTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServiceType
        fields = '__all__'
