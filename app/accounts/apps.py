###
# Libs
###
from django.apps import AppConfig


###
# Config
###
class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app.accounts'

    def ready(self):
        import app.accounts.signals