# scheduler_proj
##部署依赖
###supervisor
>在部署设备上安装supervisor 用于进行管理服务程序
>部署方式(ubuntu): apt-get install supervisor 
>启动  supervisord -c /etc/supervisor.conf
>
>配置文件,一般在 /etc/supervisor.conf  中引入 /etc/supervisor.d/*.ini  ,此后所有的程序配置均可放入此中.重新reload 即可
>各服务部署ini文件配置,格式(分flower / svr / scheduler 三个配置文件,格式如下所示,请参照部署)

```
[program:celery_flower] #指定程序名
command=/.vitualenv/dev/bin/celery  flower --broker=amqp://guest:guest@localhost//  #指定程序启动入库
redirect_stderr=true
stdout_logfile=/tmp/celery_flower.log #指定日志输出
stdout_logfile_maxbytes=5MB
stdout_logfile_backups=10
directory=/virtual_proj/proj #指定运行程序目录
user=jackyzhou #指定用户
```

```
[program:celery_svr]
command=/.vitualenv/dev/bin/celery -A proj worker  --loglevel=info
redirect_stderr=true
stdout_logfile=/tmp/celery_svr.log
stdout_logfile_maxbytes=5MB
stdout_logfile_backups=10
directory=/virtual_proj
user=jackyzhou
```

```
[program:celery_schedule]
command=/.vitualenv/dev/virtual_proj/dev1/bin/celery -A proj beat -s /tmp/celerybeat-schedule --loglevel=debug
redirect_stderr=true
stdout_logfile=/tmp/celery_schedule.log
stdout_logfile_maxbytes=5MB
stdout_logfile_backups=10
directory=/virtual_proj
user=jackyzhou
```

###virtualenv
>目的:用于管理程序运行时所需要的package,
>部署方式:
> 安装:pip install virtualenv  
> 创建虚拟环境 virtualenv dev
> 进入虚拟环境 source dev/bin/activate
> 安装相关包  pip  ....
> 退出虚拟环境 deactivate
>
###启动服务 
>进入supervisor 管理端  supervisorctl
>reload  重启 supervisor 
>restart ***  重启 *** 服务
>start ***  启动 *** 服务
>stop *** 停止 *** 服务


