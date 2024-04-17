"""
Carwash Services Constants
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
class AppointmentStatusMixin(object):
    SCHEDULED = 'scheduled'
    CONFIRMED = 'confirmed'
    IN_PROGRESS = 'in_progress'
    COMPLETED = 'completed'
    CANCELLED = 'cancelled'

    APPOINTMENT_CHOICES = [
        (SCHEDULED, _('Scheduled')),
        (CONFIRMED, _('Confirmed')),
        (IN_PROGRESS, _('In Progress')),
        (COMPLETED, _('Completed')),
        (CANCELLED, _('Cancelled')),
    ]
