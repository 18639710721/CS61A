# -*- coding: utf-8 -*-
# @Time    : 2022/12/9 23:43
# @Author  : listem
# @FileName: high_order_function.py
# @Software: PyCharm

from operator import mul


def apply_two(f, n):
    return f(f(n))


def square(n: int):
    return mul(n, n)


print(apply_two(square, 5))


def make_adder(n):
    def adder(k):
        return k + n

    return adder


three_adder = make_adder(3)
print(three_adder(4))
print(three_adder(5))
print(three_adder(6))
