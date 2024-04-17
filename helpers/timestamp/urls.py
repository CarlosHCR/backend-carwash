"""
Timestamp URL Configuration
"""
###
# Libs
###
from django.urls import path, include


###
# URL Patterns
###


urlpatterns = [
    path('api/v1/', include('helpers.timestamp.api.v1.urls'))
]
