"""
API V1: User Details Views
"""
###
# Libs
###
from rest_framework import viewsets, permissions
from rest_framework.exceptions import PermissionDenied

from app.accounts.api.v1.permissions import UserDetailsPermission
from app.accounts.api.v1.serializers.accounts.default import UserDetailsByRoleSerializer
from app.accounts.constants import UserRolesMixin
from app.accounts.models import User


###
# Viewsets
###


class UserDetailsByRoleViewSet(viewsets.ModelViewSet):
    serializer_class = UserDetailsByRoleSerializer
    permission_classes = (permissions.IsAuthenticated,
                          UserDetailsPermission)

    def get_queryset(self):
        user = self.request.user

        if user.role == UserRolesMixin.ADMIN:
            return User.objects.filter(id=user.id) \
                | User.objects.filter(role__in=[UserRolesMixin.STAFF, UserRolesMixin.CLIENT]).order_by('id')

        elif user.role == UserRolesMixin.STAFF:
            return User.objects.filter(id=user.id) \
                | User.objects.filter(role=UserRolesMixin.CLIENT).order_by('id')

        else:
            raise PermissionDenied()
