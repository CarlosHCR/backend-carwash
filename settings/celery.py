###
# Libraries
###
import os
from celery import Celery
from celery.schedules import crontab
from settings.settings import INSTALLED_APPS


###
# celery configuration
###
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.settings')

app = Celery('settings')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: INSTALLED_APPS)
