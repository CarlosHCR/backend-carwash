"""
API V1: CarWash Service Views
"""
###
# Libs
###
from django_filters import rest_framework as filters
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from app.accounts.api.v1.permissions import ClientStatusPermission, DefaultCarWashPermission, StaffStatusPermission
from app.accounts.constants import UserRolesMixin
from app.carwash.api.v1.filters.carwash_services.carwash_services import CarWashServiceFilter
from app.carwash.api.v1.serializers.carwash_services.create import CreateCarWashServiceSerializer
from app.carwash.api.v1.serializers.carwash_services.default import DefaultCarWashServiceSerializer
from app.carwash.api.v1.serializers.carwash_services.update import UpdateCarWashServiceSerializer
from app.carwash.constants import AppointmentStatusMixin
from app.carwash.models.carwash_services import CarWashService


###
# Viewsets
###
class CarWashServiceViewSet(viewsets.ModelViewSet):
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CarWashServiceFilter
    permission_classes = (permissions.IsAuthenticated,
                          DefaultCarWashPermission,)

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateCarWashServiceSerializer
        elif self.action in ['partial_update', 'update']:
            return UpdateCarWashServiceSerializer
        return DefaultCarWashServiceSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['action'] = self.action
        return context

    def get_queryset(self):
        user = self.request.user
        if user.role in [UserRolesMixin.STAFF, UserRolesMixin.ADMIN]:
            return CarWashService.objects.order_by('id')
        elif user.role == UserRolesMixin.CLIENT:
            return CarWashService.objects.filter(registered_by=user).order_by('id')
        else:
            return CarWashService.objects.none()

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(registered_by=user)

    ###
    # Actions to alter the STATUS FIELD
    ###
    # STATUS CONFIRMED
    @action(
        detail=True,
        methods=['patch'],
        url_path='confirm',
        permission_classes=(
            permissions.IsAuthenticated,
            StaffStatusPermission,
        )
    )
    def status_confirmed(self, request, pk):
        carwash_service = self.get_object()
        carwash_service.status = AppointmentStatusMixin.CONFIRMED
        carwash_service.save()

        return Response(status=status.HTTP_204_NO_CONTENT)

    # STATUS IN PROGRESS
    @action(
        detail=True,
        methods=['patch'],
        url_path='in_progress',
        permission_classes=(
            permissions.IsAuthenticated,
            StaffStatusPermission,
        )
    )
    def status_in_progress(self, request, pk):
        carwash_service = self.get_object()
        carwash_service.status = AppointmentStatusMixin.IN_PROGRESS
        carwash_service.save()

        return Response(status=status.HTTP_204_NO_CONTENT)

    # STATUS COMPLETED
    @action(
        detail=True,
        methods=['patch'],
        url_path='complet',
        permission_classes=(
            permissions.IsAuthenticated,
            StaffStatusPermission,
        )
    )
    def status_conplet(self, request, pk):
        carwash_service = self.get_object()
        carwash_service.status = AppointmentStatusMixin.COMPLETED
        carwash_service.save()

        return Response(status=status.HTTP_204_NO_CONTENT)

    # STATUS CANCELLED
    @action(
        detail=True,
        methods=['patch'],
        url_path='cancel',
        permission_classes=(
            permissions.IsAuthenticated,
            ClientStatusPermission,
        )
    )
    def status_cancel(self, request, pk):
        carwash_service = self.get_object()
        carwash_service.status = AppointmentStatusMixin.CANCELLED
        carwash_service.save()

        return Response(status=status.HTTP_204_NO_CONTENT)
