"""
Carwash Services URL Configuration
"""
###
# Libs
###
from django.urls import path, include


###
# URL Patterns
###


urlpatterns = [
    path('api/v1/', include('app.carwash.api.v1.urls'))
]
