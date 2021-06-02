from django.urls import path

from . import views

urlpatterns = [
    path('', views.list_persons, name='list_persons'),
    path('add/', views.add_person_via_celery, name='add_person_via_celery'),
]
