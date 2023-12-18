from __future__ import absolute_import
import os

import environ
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

# set the default Django settings module for the 'celery' program.

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.production')
environ.Env.read_env('../.env')

app = Celery('config')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.beat_schedule = {
    # 'test-task': {
    #     'task': 'config.tasks.add',
    #     'schedule': crontab(),
    # },
}

'''
crontab() - every minute
crontab(minute='*/15') - every 15 minutes
crontab(minute=0, hour='*') - every hour
crontab(minute=0, hour='*/3') - every 3 hours
crontab(minute=0, hour=0) - daily midnight
'''


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
