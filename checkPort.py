# -*- coding:utf-8 -*-
import socket               #使用socket模块的socket.stocket.connect_ex函数来判断端口是否可以联通
import time,os

port_List=[20,30,80,1540,1539,3306,8080]

for port in port_List:
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    check_result=sock.connect_ex(('127.0.0.1',port))#connect_ex,返回一个connect的error结果
    if check_result == 0:
        print("Port {} is open".format(port))
    else:
        print("Port {} is not open".format(port))
