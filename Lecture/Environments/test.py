# -*- coding: utf-8 -*-
# @Time    : 2022/12/10 13:24
# @Author  : listem
# @FileName: test.py
# @Software: PyCharm

"""
Higher-Order Functions
    A function that takes a function as an argument value or
    returns a function as a return value


"""

import time

print("---RUNOOB EXAMPLE ： Loading 效果---")

print("Loading", end="")
for i in range(20):
    print(".", end='', flush=True)
    time.sleep(0.5)


