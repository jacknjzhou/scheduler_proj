#!-*-encoding:utf8-*-
from __future__ import absolute_import
from proj.celery import app
import random
import time
from celery.task import Task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

class MyTask(Task):

    def on_success(self,retval,task_id,args,kwargs):
        print "task done:{0}".format(retval)

        return super(MyTask, self).on_success(retval,task_id,args,kwargs)
    def on_failure(self,exc,task_id,args,kwargs,einfo):
        print "task fail,reason:{0}".format(exc)
        return super(MyTask,self).on_failure(exc,task_id,args,kwargs,einfo)

    def after_return(self,status,retval,task_id,args,kwargs,einfo):
        print "after retrun,status:{0}".format(status)
        return super(MyTask,self).after_return(status,retval,task_id,args,kwargs,einfo)

@app.task(base=MyTask,bind=True)
def add(self,x, y):
    print "******[add]*******"
    if x == -1:
        x = random.randint(0,1000000)
    if y == -1:
        y = random.randint(2000000,1100000000)
    logger.info(self.request.__dict__)
    return x+y

@app.task()
def task_A(x,y):
    print "task_A:[x="+str(x)+",y="+str(y)+"]"
    return x + y

@app.task()
def task_B(x,y):
    print "task_B:[x="+str(x)+",y="+str(y)+"]"
    return x + y

@app.task(bind=True)
def test_mes(self):
    for i in xrange(1,11):
        time.sleep(0.1)
        self.update_status(status="PROGRESS",meta={'p':i*10})
    return 'Finish'
