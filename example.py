#coding:utf8
'''
用法
from example import root
'''
from bottle import route

@route('/')
def root():
    u'''根目录'''
    return 'Hello!!!'


