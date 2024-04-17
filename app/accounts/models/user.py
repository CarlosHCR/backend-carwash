###
# Libs
###
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _

from app.accounts.constants import UserRolesMixin


###
# Model
###
class User(AbstractUser):
    phone_number = models.CharField(
        max_length=20,
        verbose_name=_('Phone Number'),
    )
    role = models.CharField(
        max_length=16,
        choices=UserRolesMixin.ROLE_CHOICES,
        default=UserRolesMixin.CLIENT,
        verbose_name=_('role')
    )
    email = models.EmailField(
        unique=True,
        max_length=254,
        verbose_name=_('email address')
    )
