# -*- coding: utf-8 -*-
# @Time    : 2022/1/9 17:00
# @Author  : listem
# @FileName: 07Fibonacci.py
# @Software: PyCharm

"""
佩波纳契数列
    递归定义
    f0 = 0
    f1 = 1
    fn = f(n-1) + f(n-2)
    任意一个数字都等于前两数之和
    1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377 ,610, 987

"""


def FiboacciSuquence(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    else:
        return FiboacciSuquence(n - 1) + FiboacciSuquence(n - 2)


if __name__ == '__main__':
    print(FiboacciSuquence(5))  # 从0开始
