from django.http import HttpResponse
from django.shortcuts import render
from .models import Person
from .tasks import add_person_to_db


def add_person_via_celery(request):
    name = request.POST["name"]
    add_person_to_db.delay(name)
    html = "Started celery task to add %s to DB!" % name
    return HttpResponse(html)


def list_persons(request):
    persons = Person.objects.all().order_by('-id')
    return render(request, 'hello_world/list_persons.html', {'persons': persons})
