"""
account admin
"""
###
# Libs
###
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from app.accounts.models.user import User


###
# Inline Admin Models
###


###
# Main Admin Models
###
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'phone_number', 'username', 'is_active',
                    'last_login', 'date_joined', 'role')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {
         'fields': ('first_name', 'last_name', 'email', 'phone_number')}),
        (_('Permissions'), {'fields': ('role', 'is_active', 'is_staff',
         'is_superuser',  'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )


admin.site.register(User, UserAdmin)
