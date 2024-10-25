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
            start_date += timedelta(days=2)

        end_date = start_date + timedelta(days=7)

        busy_times = set(
            CarWashService.objects.filter(
                service_date__range=[start_date, end_date]
            ).values_list('service_date', flat=True)
        )

        available_times = [
            tz.localtime(tz.make_aware(datetime.combine(
                start_date + timedelta(days=day), time)))
            for day in range((end_date - start_date).days + 1)
            for time in [datetime.strptime('07:00', '%H:%M').time(), datetime.strptime('13:00', '%H:%M').time()]
        ]

        available_times = [
            time for time in available_times if time not in busy_times]

        return Response(available_times)
