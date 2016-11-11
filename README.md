##### server.py
主服务脚本，可自行定义各种接口

##### server.conf
服务配置文件,定义服务主机地址，端口号

##### setting.py
读取配置文件内容

##### log.py
日志模块

##### keep_alive.py
定期监测服务是否正常，需添加定时任务
```
*/5 * * * * /usr/bin/python /work/server_forever/keep_alive.py
```
##### example.py
示例用法
