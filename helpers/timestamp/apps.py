###
# Libs
###
from django.apps import AppConfig


###
# Config
###
class TimestampConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'helpers.timestamp'

    def ready(self):
        import helpers.timestamp.signals