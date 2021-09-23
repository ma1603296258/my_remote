'''
Author: your name
Date: 2021-08-03 19:01:31
LastEditTime: 2021-09-11 00:51:22
LastEditors: your name
Description: In User Settings Edit
FilePath: \py\py\File.py
'''
# Python open() 方法用于打开一个文件，并返回文件对象，在对文件进行处理
# 过程都需要使用到这个函数，如果该文件无法被打开，会抛出 OSError。
# note: 使用 open() 方法一定要保证关闭文件对象，即调用 close() 方法。
# open() 函数常用形式是接收两个参数：文件名(file)和模式(mode)。
'''
 open(file, mode='r')
# 完整的语法格式
open(file, mode='r', buffering=-1, encoding=None, errors=None, 
     newline=None, closefd=True, opener=None)
'''
# 参数说明
# file: 必需，文件路径         mode: 可选，文件打开模式
# buffering: 设置缓冲         encoding: 一般使用utf8
# errors: 报错级别            newline: 区分换行符
# closefd: 传入的file参数类型
# opener: 设置自定义开启器，开启器的返回值必须是一个打开的文件描述符。

# file object
# file 对象使用 open 函数来创建，下表列出了 file 对象常用的函数：
