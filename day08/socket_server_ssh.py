8
import socket
import os

server = socket.socket()
server.bind(("localhost", 8888))
server.listen()

while True:
    conn,addr = server.accept()
    print("new conn",addr)
    while True:
        data = conn.recv(2048)  #1024 ipconfig命令报错，换成2048能执行
        if not data:
            print("client is not connecting...")
            break
        print("执行指令")
        cmd_res = os.popen(data.decode()).read() #接受字符串，返回也是字符串
        print("before send", len(cmd_res))
        if len(cmd_res) == 0:
            cmd_res = "cmd has no output..."
        conn.send(cmd_res.encode("utf-8"))
        print("send done")
server.close()