# !/usr/bin/env python
# _*_ coding:utf-8 _*_

import socket
import os
import hashlib

server = socket.socket()
server.bind(("localhost", 8888))
server.listen()

while True:
    conn,addr = server.accept()
    print("new conn",addr)
    while True:
        print("等待新指令")
        data = conn.recv(1024)
        if not data:
            print("client is not connecting...")
            break
        cmd,filename = data.decode().split()
        print(filename)
        if os.path.isfile(filename):
            f = open(filename,"rb")
            m = hashlib.md5()
            file_size = os.stat(filename).st_size
            conn.send(str(file_size).encode())  #send file size
            conn.recv(1024) #wait for ack
            for line in f:
                m.update(line)
                conn.send(line)
            print("file md5", m.hexdigest())
            f.close()
            conn.send(m.hexdigest().encode()) #send md5 to client
        print("send done")
server.close()