# !/usr/bin/env python
# _*_ coding:utf-8 _*_

import shutil

f1 = open("本节笔记", encoding= "utf-8")

f2 = open("笔记2", "w", encoding= "utf-89")

shutil.copyfileobj(f1, f2)