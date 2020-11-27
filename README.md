# Django Celery Proof of Concept

Simple POC of using [Celery](https://docs.celeryproject.org/en/stable/index.html) task queue in Django.

Configured with [Redis](https://redis.io) as message broker. Redis is a in-memory data store often used in Django.

A more recommended setup is to use [RabbitMQ](https://www.rabbitmq.com), the most widely used open-source message broker.
This is a persistent storage system that maintains the task queue even if the server crashes.

### More info

[Setting up an asynchronous task queue for Django using Celery and Redis. Michal Karzynski. 2014](http://michal.karzynski.pl/blog/2014/05/18/setting-up-an-asynchronous-task-queue-for-django-using-celery-redis/)

## Essential files

For essential files see commit [de02fa2](https://github.com/jontingvold/django-celery-oc/commit/ebe334ca0a12fa65ac385bbbba09c00737c7b2a8).

## Installation and startup of Redis and Celery

#### Install and start Redis (mac)

`brew install redis`
`brew services start redis`

#### Install Celery

`pip install -U "celery[redis]"`

#### Start Celery

`celery --app=django_celery_poc.celery:app worker --loglevel=INFO`

For a production server, Celery should be set up as a service.
