# !/usr/bin/env python
# _*_ coding:utf-8 _*_
import gevent

def foo():
    print("running in foo")
    gevent.sleep(2)
    print("explicit context switch to foo again")

def bar():
    print("explicit context to bar")
    gevent.sleep(1)
    print("Implicit context switch back to bar")

def func3():
    print("running in func3")
    gevent.sleep(0)
    print("running in func3 again")
gevent.joinall([
    gevent.spawn(foo),
    gevent.spawn(bar),
    gevent.spawn(func3)
])