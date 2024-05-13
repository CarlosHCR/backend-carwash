"""
API V1: Busy Times Views
"""
###
# Libs
###
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime, timedelta
from django.utils import timezone as tz
import pytz

from settings.settings import TIME_ZONE
from app.carwash.models.carwash_service import CarWashService

timezone = pytz.timezone(TIME_ZONE)

###
# Viewsets
###


class BusyTimesView(APIView):

    def post(self, request):
        date_selected = request.data.get('date')

        if date_selected:
            try:
                start_date = datetime.strptime(
                    date_selected, '%Y-%m-%d').date()
            except ValueError:
                return Response({'error': 'Invalid date.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            start_date = tz.now().date()

        if start_date == tz.now().date():
            start_date += timedelta(days=1)

        end_date = start_date + timedelta(days=7)

        busy_times = CarWashService.objects.filter(
            service_date__date__range=[
                start_date, end_date
            ]
        ).values_list('service_date', flat=True)

        available_times = []

        for day in range((end_date - start_date).days + 1):
            date = start_date + timedelta(days=day)

            time_0700 = timezone.localize(datetime.combine(
                date, datetime.strptime('07:00', '%H:%M').time()))
            time_1300 = timezone.localize(datetime.combine(
                date, datetime.strptime('13:00', '%H:%M').time()))

            available_times.append(time_0700)
            available_times.append(time_1300)

        for busy_time in busy_times:
            if busy_time in available_times:
                available_times.remove(busy_time)

        return Response(available_times)
