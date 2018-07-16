# !/usr/bin/env python
# _*_ coding:utf-8 _*_
import socket

client = socket.socket()
client.connect(("localhost", 6969))
client.send(b"helloworld")
data = client.recv(1024)

print("recv：",data)
client.close()