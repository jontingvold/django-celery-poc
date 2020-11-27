from __future__ import absolute_import
from .models import Person

from celery import shared_task

@shared_task
def add_person_to_db(name):
    person = Person(name=name)
    person.save()
