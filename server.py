#coding:utf8
'''
bottle 服务框架
自定义 各种接口
'''
import os
import json

from bottle import run, route, request, response

import log
import setting

cur_path = os.path.dirname(os.path.abspath(__file__))

# 保存 pid
pid = os.getpid()
with open(os.path.join(cur_path, 'pid'), 'w') as f:
    f.write(str(pid))

#@route('/')
#def root():
#    u'''根目录'''
#    return 'Hello!!!'
from example import root

@route('/pid')
def get_pid():
    return str(pid)

run(host=setting.HOST, port=setting.PORT, server='paste')
