#coding:utf8
'''
定期检查服务是否正常并重启
*/5 * * * * /usr/bin/python /work/server_forever/keep_alive.py &
'''
import os
import urllib2

import log
import setting

cur_path = os.path.dirname(os.path.abspath(__file__))


def get_python_path():
    '''获取 python 执行路径'''
    with os.popen('which python') as f:
        s = f.read()
    return s.strip()

# python 执行路径
python_path = get_python_path()
# pid 文件路径
pid_path = os.path.join(cur_path, 'pid')

def get_pid():
    u'''获取pid'''
    pid = 0
    if os.path.exists(pid_path):
        with open(pid_path) as f:
            pid = f.read().strip()
    return int(pid) if pid else 0

def server_alive():
    u'''
    检查 server 是否存活
    调用默认 pid 接口判断 
    '''
    try:
        pid = urllib2.urlopen('http://%s:%s/pid'%(setting.HOST, setting.PORT), timeout=10).read()
        pid = int(pid.strip())
        return pid
    except Exception as e:
        log.logger.exception(e)
    return 0
        
def main():
    # 检查服务是否正常
    if not server_alive():
        # 不正常则重启 使用守护进程模式
        os.system('%s %s &'%(python_path, os.path.join(cur_path, 'server.py ')))
    return 1

if __name__ == "__main__":
    main()
