# !/usr/bin/env python
# _*_ coding:utf-8 _*_


#内部方法：
#lib = __import__("lib.aa")
#print(lib.aa.C().name)


#官方推荐方法

import importlib
aa = importlib.import_module("lib.aa")
print(aa.C().name)