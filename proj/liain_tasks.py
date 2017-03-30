#!-*-encoding:utf8-*-
#!-*-encoding:utf8-*-
from __future__ import absolute_import
from proj.celery import app
import random
import time
from celery.task import Task
from celery.utils.log import get_task_logger


logger = get_task_logger(__name__)

class LiainTask(Task):
    def on_success(self,retval,task_id,args,kwargs):
        print "task done:{0}".format(retval)

        return super(MyTask, self).on_success(retval,task_id,args,kwargs)
    def on_failure(self,exc,task_id,args,kwargs,einfo):
        print "task fail,reason:{0}".format(exc)
        return super(MyTask,self).on_failure(exc,task_id,args,kwargs,einfo)


