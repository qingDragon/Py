# !/usr/bin/env python
# _*_ coding:utf-8 _*_


def func(self):
    print('hello %s' %self.name)


def __init__(self,name,age):
    self.name = name
    self.age = age

Foo = type('Foo', (object,), {'talk':func,'__init__':__init__})
f = Foo("yz",22)
f.talk()
print(type(Foo))