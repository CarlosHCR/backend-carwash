"""
API V1: CarWash Service Filters
"""
###
# Libs
###
from django_filters import rest_framework as filters

from app.carwash.models.carwash_services import CarWashService


###
# Filters
###


class CarWashServiceFilter(filters.FilterSet):
    day = filters.NumberFilter(method='filter_day')
    month = filters.NumberFilter(method='filter_month')
    year = filters.NumberFilter(method='filter_year')
    service_date = filters.DateFilter(method='filter_service_date')
    vehicle_license_plate_number = filters.CharFilter(
        method='filter_vehicle_license_plate_number')

    def filter_day(self, queryset, name, value):
        return queryset.filter(service_date__day=value)

    def filter_month(self, queryset, name, value):
        return queryset.filter(service_date__month=value)

    def filter_year(self, queryset, name, value):
        return queryset.filter(service_date__year=value)

    def filter_service_date(self, queryset, name, value):
        return queryset.filter(service_date=value)

    # ?day=24&year=2024

    # ?day=28&month=01&year=2024

    # ?service_date=2024-01-28

    def filter_vehicle_license_plate_number(self, queryset, name, value):
        return queryset.filter(vehicle_license_plate__number__icontains=value)

    class Meta:
        model = CarWashService
        fields = ['day', 'month', 'year', 'service_date',
                  'vehicle_license_plate_number']
