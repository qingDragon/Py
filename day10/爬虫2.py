# !/usr/bin/env python
# _*_ coding:utf-8 _*_

from urllib import request
import gevent,time
from gevent import monkey

monkey.patch_all() #把当前程序的所有io操作打上记号

def f(url):
    print("GET:%s" % url)
    resp = request.urlopen(url)
    data = resp.read()
    print("%d bytes received from %s."%(len(data),url))

urls = [
    'https://www.python.org/',
    'https://www.yahoo.com/',
    'https://github.com/'
    ]

time_start = time.time()
for url in urls:
    f(url)

print("同步cost:",time.time()-time_start)

asvnc_time_start = time.time()
gevent.joinall([
    gevent.spawn(f,"https://www.python.org/"),
    gevent.spawn(f, "https://www.yahoo.com/"),
    gevent.spawn(f, "https://github.com/")
])
print("异步cost:",time.time()-asvnc_time_start)