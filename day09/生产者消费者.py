# !/usr/bin/env python
# _*_ coding:utf-8 _*_
import queue
import threading,time

q = queue.Queue(maxsize=10)

def Producer(name):
    count = 1
    while True:
        q.put("骨头%s" % count)
        print("[%s]生产了骨头%s"% (name,count))
        count += 1
        time.sleep(0.1)


def Consumer(name):
    # while q.qsize()>0:
    while True:
        print("[%s]取到[%s]并且吃了它" %(name,q.get()))
        time.sleep(1)

p = threading.Thread(target=Producer,args=("yz",))
c = threading.Thread(target=Consumer, args=("张朔",))
c1 = threading.Thread(target=Consumer, args=("guyang",))
p.start()
c.start()
c1.start()
