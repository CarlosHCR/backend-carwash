##
# Libs
##
from django.urls import include, path
from rest_framework import routers

###
# Routers
###
router = routers.DefaultRouter()

###
# URLs
###
urlpatterns = [
    path('', include(router.urls)),

]
