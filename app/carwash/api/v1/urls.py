"""
API V1: Carwash Services Urls
"""
###
# Libs
###
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app.carwash.api.v1.views.carwash_service import CarWashServiceViewSet
from app.carwash.api.v1.views.service_type import ServiceTypeViewSet
from app.carwash.api.v1.views.vehicle_license_plate import VehicleLicensePlateViewSet
from app.carwash.api.v1.views.busy_times import BusyTimesView

###
# Routers
###
""" Main router """
router = DefaultRouter()

router.register(
    r'carwashservice',
    CarWashServiceViewSet,
    basename='carwashservice'
)
router.register(
    r'servicetypes',
    ServiceTypeViewSet,
    basename='servicetype'
)
router.register(
    r'vehiclelicenseplate',
    VehicleLicensePlateViewSet,
    basename='vehiclelicenseplates'
)


###
# URLs
###
urlpatterns = [
    path('', include(router.urls)),
    path('busytimes/', BusyTimesView.as_view(), name='busy_times'),
]
