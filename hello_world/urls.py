from django.urls import path

from . import views

urlpatterns = [
    path('', views.list_persons, name='list_persons'),
    path('<name>/', views.add_person, name='add_person'),
    path('celery/<name>/', views.add_person_via_celery, name='add_person_via_celery'),
]
