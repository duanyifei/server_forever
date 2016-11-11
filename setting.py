#coding:utf8
'''
配置文件读取
'''
import os
import ConfigParser

# 获取当前路径
cur_path = os.path.dirname(os.path.abspath(__file__))
# 获取配置文件路径
conf_path = os.path.join(cur_path, 'server.conf')

# 初始化配置对象
config = ConfigParser.ConfigParser()
# 读取配置文件内容
config.read(conf_path)


# HOST 主机地址
HOST = config.get('server', 'host')
# PORT 服务端口
PORT = config.getint('server', 'port')


if __name__ == "__main__":
    print HOST
    print PORT
