


import socket




client = socket.socket()
client.connect(("localhost",8888))

while True:
    cmd = input(">>:").strip()
    if len(cmd) == 0:
        continue
    client.send(cmd.encode("utf-8"))

    cmd_res = client.recv(2048)
    print(cmd_res.decode())
client.close()
