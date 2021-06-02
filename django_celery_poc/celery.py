# Setup of Celery for background tasks
# https://docs.celeryproject.org/en/latest/django/first-steps-with-django.html

from __future__ import absolute_import

import os
from celery import Celery
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery_poc.settings')

app = Celery('django_celery_poc')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# Celery Once Configuration
if settings.CELERY_ALWAYS_EAGER:
    app.conf.ONCE = {
        'backend': 'django_celery_poc.celery_once.custom_backends.TrivialEagerBackend',
        'settings': {},
    }
else:
    app.conf.ONCE = {
        'backend': 'celery_once.backends.Redis',
        'settings': {
            'url': settings.CELERY_ONCE_REDIS_URL,
            'default_timeout': 60 * 60
        }
    }


# Celery Beats configuration, periodic jobs
app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'hello_world.tasks.add_person_to_db_queue_many',
        'schedule': 30.0,
        'args': ["Add automatically"]
    },
}


# Test Celery and Celery Once at startup
# – It is always nice with early failure

from celery import shared_task
from celery_once import QueueOnce

@shared_task(base=QueueOnce, once={'graceful': True})
def test_celery_and_celery_once():
    pass

test_celery_and_celery_once.delay()
