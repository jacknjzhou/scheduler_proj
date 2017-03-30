#!-*-encoding:utf8-*-
from __future__ import absolute_import
from celery import Celery
from proj.celeryconfig import BROKER_URL
#from proj.celeryconfig import BACKEND_URL

app = Celery('proj',include=['proj.tasks'])
#app = Celery('proj',backend=BACKEND_URL,broker=BROKER_URL,include=['proj.tasks'])
app.config_from_object('proj.celeryconfig')

if __name__ == '__main__':
	app.start()
