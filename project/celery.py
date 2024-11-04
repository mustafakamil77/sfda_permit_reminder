
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

app = Celery('project')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.enable_utc = False

app.conf.update(timezone = 'Asia/Riyadh')

app.autodiscover_tasks()


    
# CELERY BEAT SETTINGS
app.conf.beat_schedule = {
    
    'send-ad-mail-every-day': {
        'task': 'sender.tasks.check_permit_expiry',
        'schedule': crontab(hour=7, minute=10),
    }
}