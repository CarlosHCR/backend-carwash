###
# Libs
###
from rest_framework.permissions import BasePermission

from app.accounts.constants import UserRolesMixin


###
# Car Wash Service Permissions
###


class DefaultCarWashPermission(BasePermission):

    def has_permission(self, request, view):
        return request.user.role in dict(UserRolesMixin.ROLE_CHOICES).keys()

    def has_object_permission(self, request, view, obj):
        if request.user.role in [UserRolesMixin.ADMIN, UserRolesMixin.STAFF]:
            return True

        if request.user.role == UserRolesMixin.CLIENT and obj.registered_by == request.user:
            return True

        return False


###
# Car Wash Status Permissions
###


class ClientStatusPermission(BasePermission):

    def has_permission(self, request, view):
        return request.user.role in dict(UserRolesMixin.ROLE_CHOICES).keys()

    def has_object_permission(self, request, view, obj):
        if request.user.role in [UserRolesMixin.ADMIN, UserRolesMixin.STAFF]:
            return True

        if request.user.role == UserRolesMixin.CLIENT and \
                obj.registered_by == request.user:
            return True
        return False


class StaffStatusPermission(BasePermission):

    def has_permission(self, request, view):
        return request.user.role in [UserRolesMixin.STAFF, UserRolesMixin.ADMIN]

    def has_object_permission(self, request, view, obj):
        if request.user.role in [UserRolesMixin.ADMIN, UserRolesMixin.STAFF]:
            return True
        return False

###
# Service Type Permissions
###


class ServiceTypeStaffPermission(BasePermission):

    def has_permission(self, request, view):
        return request.user.role in [UserRolesMixin.STAFF, UserRolesMixin.ADMIN]
