"""
Carwash Services admin
"""
###
# Libs
###
from django.contrib import admin

from app.carwash.admin.vehicle_license_plate import VehicleLicensePlateForm
from app.carwash.models.carwash_services import CarWashService
from app.carwash.models.service_type import ServiceType
from app.carwash.models.vehicle_license_plate import VehicleLicensePlate


###
# Inline Admin Models
###


###
# Main Admin Models
###
class CarwashServicesAdmin(admin.ModelAdmin):
    """
    Carwash Services Admin
    """
    list_display = (
        'id',
        'registered_by',
        'vehicle_license_plate',
        'price',
        'service_type',
        'service_date',
        'status',
        'notes',
    )

    fieldsets = (
        ('Model Fields', {
            'fields': ('price', 'service_date', 'status', 'notes')
        }),
        ('Relationships', {
            'fields': ('registered_by', 'vehicle_license_plate', 'service_type',)
        }),
    )


class ServiceTypeAdmin(admin.ModelAdmin):
    """
    Service Type Admin
    """
    list_display = (
        'id',
        'name',
        'price',
        'is_active',
        'created_at',
        'updated_at',
    )


class VehicleLicensePlateAdmin(admin.ModelAdmin):
    """
    Vehicle License Plate Admin
    """
    list_display = (
        'id',
        'number',
        'created_at',
        'updated_at',
    )
    form = VehicleLicensePlateForm


admin.site.register(CarWashService, CarwashServicesAdmin)
admin.site.register(ServiceType, ServiceTypeAdmin)
admin.site.register(VehicleLicensePlate, VehicleLicensePlateAdmin)
