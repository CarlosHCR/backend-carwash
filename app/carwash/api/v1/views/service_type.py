"""
API V1: Service Type Views
"""
###
# Libs
###
from rest_framework import viewsets, permissions

from app.accounts.api.v1.permissions import ServiceTypeStaffPermission
from app.carwash.api.v1.serializers.service_type.default import DefaultServiceTypeSerializer
from app.carwash.models.service_type import ServiceType


###
# Viewsets
###


class ServiceTypeViewSet(viewsets.ModelViewSet):
    queryset = ServiceType.objects.all().order_by('id')
    serializer_class = DefaultServiceTypeSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [permissions.IsAuthenticated,]
        else:
            self.permission_classes = [
                permissions.IsAuthenticated, ServiceTypeStaffPermission]
        return super(ServiceTypeViewSet, self).get_permissions()

    def get_queryset(self):
        if self.request.user.role in ['staff', 'admin']:
            return self.queryset.order_by('id')
        return self.queryset.filter(is_active=True)
