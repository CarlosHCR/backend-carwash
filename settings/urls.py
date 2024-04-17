"""
Root URL Configuration
"""
###
# Libs
###
from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Swagger Config
schema_view = get_schema_view(
    openapi.Info(
        title="Carwash",
        default_version='v1',
        description="Carwash Backend",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.accounts.urls')),
    path('', include('app.carwash.urls')),

    # Swagger urls
    path('swagger', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),

]
