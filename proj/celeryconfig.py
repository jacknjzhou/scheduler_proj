#!-*-encoding:utf8-*-
from __future__ import absolute_import 
from celery.schedules import crontab
from kombu import Queue, Exchange
#import random

BROKER_URL='amqp://guest:guest@localhost:5672//'
#BACKEND_URL='file:///Volumes/data/tmp/celery_backend_result'
CELERY_RESULT_BACKEND='redis://localhost:6379/1'

CELERY_TASK_SERIALIZER='json'
CELERY_RESULT_SERIALIZER='json'
CELERY_TASK_RESULT_EXPIRES=600
CELERY_ACCEPT_CONTENT=['json','msgpack']

CELERY_DEFAULT_EXCHANGE = 'oss.partner'
#CELERY_DEFAULT_EXCHANGE_TYPE = 'topic'
#CELERY_DEFAULT_QUEUE = 'oss.partner.default' 

CELERY_TIMEZONE = 'Asia/Shanghai'
CELERY_ENABLE_UTC = False

CELERY_LOG_FILE='/tmp/celery_proj.log'

CELERYBEAT_SCHEDULE = {
    'add':{'task':'proj.tasks.add','schedule':crontab('*/60'),
            'args':(-1,-1)}
}

CELERY_QUEUES = (
    Queue('add',Exchange('add'),routing_key='add'),
    Queue('task_A',Exchange('task_A'),routing_key='task_A'),
    Queue('task_B',Exchange('task_B'),routing_key='task_B')
    )

CELERY_ROUTES = {
    'proj.tasks.add':{'queue':'add','routing_key':'add'},
    'proj.tasks.task_A':{'queue':'task_A','routing_key':'task_A'},
    'proj.tasks.task_B':{'queue':'task_B','routing_key':'task_B'}
}