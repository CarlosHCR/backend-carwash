"""
API V1: Busy Times Views
"""
###
# Libs
###
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime, timedelta, time
from django.utils import timezone
from django.utils.timezone import make_aware


from app.carwash.models.carwash_service import CarWashService


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
                start_date = timezone.now().date()

            if start_date == timezone.now().date():
                start_date += timedelta(days=2)

            end_date = start_date + timedelta(days=7)

            busy_times = set(CarWashService.objects.filter(
                service_date__range=[start_date, end_date]
            ).values_list('service_date', flat=True))

            time_slots = [time(7, 0), time(13, 0)]

            available_times = [
                make_aware(datetime.combine(date, slot))
                for date in [start_date + timedelta(days=day) for day in range((end_date - start_date).days + 1)]
                for slot in time_slots
            ]

            available_times = [
                t for t in available_times if t not in busy_times]

            return Response(available_times, status=status.HTTP_200_OK)
