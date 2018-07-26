# !/usr/bin/env python
# _*_ coding:utf-8 _*_

from greenlet import greenlet
#greenlet仍然是手动切换

def test1():
    print(12)
    gr2.switch()
    print(34)
    gr2.switch()

def test2():
    print(56)
    gr1.switch()
    print(78)


gr1 = greenlet(test1) #启动一个协程
gr2 = greenlet(test2)
gr1.switch()
