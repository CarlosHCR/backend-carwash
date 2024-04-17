"""
account Constants
"""
###
# Libs
###
from django.utils.translation import gettext as _

###
# Choices
###

###
# Constants Mixins
###
class UserRolesMixin(object):
    CLIENT = 'client'
    STAFF = 'staff'
    ADMIN = 'admin'

    ROLE_CHOICES = [
        (CLIENT, _('Client')),
        (STAFF, _('Staff')),
        (ADMIN, _('Administrator')),
    ]
