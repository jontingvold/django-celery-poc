# Django Celery Proof of Concept

Simple POC of using [Celery](https://docs.celeryproject.org/en/stable/index.html) task queue in Django.

Configured with [Redis](https://redis.io) as message broker. Redis is a in-memory data store often used in Django.

A more recommended setup is to use [RabbitMQ](https://www.rabbitmq.com), the most widely used open-source message broker.
This is a persistent storage system that maintains the task queue even if the server crashes.

### More info

[Setting up an asynchronous task queue for Django using Celery and Redis. Michal Karzynski. 2014](http://michal.karzynski.pl/blog/2014/05/18/setting-up-an-asynchronous-task-queue-for-django-using-celery-redis/)

## Essential files

For essential files see commit [5af6995](https://github.com/jontingvold/django-celery-poc/commit/5af69952d6fe28b7204bf3081137e01f3aaacc04).

## Installation and startup of Redis and Celery

#### Install and start Redis (mac)

`brew install rabbitmq`
`brew services start rabbitmq`

#### Install Celery

`pip install -U "celery[rabbitmq]"`

#### Start Celery

Start Django:
`python manage.py runserver`

Start worker:
`celery -A django_celery_poc worker`

Start beat worker (can not be more than one):
`celery -A django_celery_poc beat`
(Can also be started together with a worker with `celery -A django_celery_poc worker -B`)

To monitor tasks, start Flower:
`celery -A django_celery_poc flower`

For a production server, Celery should be set up as a service.
