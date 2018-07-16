# !/usr/bin/env python
# _*_ coding:utf-8 _*_
import socket

server = socket.socket()
server.bind(("localhost",6969))

server.listen()
print("我要开始等电话了")
conn,addr = server.accept()
print(conn,addr)
print("电话来了")
data = conn.recv(1024)
print("server_recv:",data)
conn.send(data.upper())
server.close()