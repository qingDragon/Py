# !/usr/bin/env python
# _*_ coding:utf-8 _*_


import threading
import time

event = threading.Event()


def lighter():
    count = 0
    event.set() #先设置绿灯
    while True:
        if count>5 and count<10 :
            event.clear()
            print("\033[41;1mred light is on...\033[0m")
        elif count>10:
            event.set() #变绿灯
            count = 0
        else:
            print("\033[42;1mgreen light is on...\033[0m")
        time.sleep(1)
        count += 1

def car(name):
    while True:
        if event.is_set():
            print("[%s] running..."% name)
            time.sleep(1)
        else:
            print("[%s] sees red light, waiting..."%name)
            event.wait()
            print("\033[34;1m[%s] green light is on ,start going..." % name)
light = threading.Thread(target=lighter,)
light.start()
car = threading.Thread(target=car,args=("Tesla",))
car.start()