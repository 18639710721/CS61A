# -*- coding: utf-8 -*-
# @Time    : 2022/12/9 14:37
# @Author  : listem
# @FileName: fib_sequence.py
# @Software: PyCharm


# 0 1 1 2 3 4 5 返回任意大于等于1的兔子数列的值
def fib(n: int):
    pre, cur = 0, 1
    for i in range(1, n):
        pre, cur = cur, pre + cur
    return cur


print(fib(3))
