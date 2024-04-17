###
# Libs
###
from django.apps import AppConfig


###
# Config
###
class CarwashConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app.carwash'
    
    def ready(self):
        import app.carwash.signals
