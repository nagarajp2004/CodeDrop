from __future__ import absolute_import
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# Add this block to schedule daily tasks at 7 AM
app.conf.beat_schedule = {
    'daily-snippet-email': {
        'task': 'snippets.tasks.send_next_snippet_email_to_all_users',
        'schedule': crontab(hour=7, minute=0),
    },
}
