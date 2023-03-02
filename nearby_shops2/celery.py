from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nearby_shops2.settings')

app = Celery('nearby_shops2')

#Default celery timezone is utc so disable it.
app.conf.enable_utc = False
app.conf.update(timezone = 'Africa/Nairobi')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')


# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

# prints all the metadata about the request when the task is received.
@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))