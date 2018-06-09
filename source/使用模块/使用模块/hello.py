#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
第一句注释，用于给Mac/Linux/Unix的用户也可以执行此代码
第二句注释，限定使用utf-8编译方式运行脚本，使其支持中文能力较好
'''

' a test module '

__author__ = 'Kark Li'

import sys

def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':#此句的作用是判断该脚本是否为一个单独运行的脚本而不是被import的脚本
    test()

#如何定义私有函数呢？
#使用_前缀
#私有函数是提醒使用者不应该被引用，做不到不能被引用
def _private_1(name):
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)

print(greeting('Kark'))