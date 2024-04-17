"""
API V1: Carwash Services Urls
"""
###
# Libs
###
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app.carwash.api.v1.views.carwash_services import CarWashServiceViewSet
from app.carwash.api.v1.views.service_type import ServiceTypeViewSet
from app.carwash.api.v1.views.vehicle_license_plate import VehicleLicensePlateViewSet


###
# Routers
###
""" Main router """
router = DefaultRouter()

router.register(
    r'carwashservices',
    CarWashServiceViewSet,
    basename='carwashservices'
)
router.register(
    r'servicetypes',
    ServiceTypeViewSet,
    basename='servicetypes'
)
router.register(
    r'vehiclelicenseplates',
    VehicleLicensePlateViewSet,
    basename='vehiclelicenseplates'
)

###
# URLs
###
urlpatterns = [
    path('', include(router.urls)),
]
