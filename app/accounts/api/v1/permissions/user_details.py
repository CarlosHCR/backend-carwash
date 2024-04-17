###
# Libs
###
from rest_framework.permissions import BasePermission

from app.accounts.constants import UserRolesMixin


###
# User Details Permissions
###
class UserDetailsPermission(BasePermission):

    def has_permission(self, request, view):
        return request.user.role in [UserRolesMixin.ADMIN, UserRolesMixin.STAFF]

    def has_object_permission(self, request, view, obj):
        if request.user.role == UserRolesMixin.ADMIN and (obj == request.user or obj.role in [UserRolesMixin.STAFF, UserRolesMixin.CLIENT]):
            return True

        elif request.user.role == UserRolesMixin.STAFF and (obj == request.user or obj.role == UserRolesMixin.CLIENT):
            return True

        return False
