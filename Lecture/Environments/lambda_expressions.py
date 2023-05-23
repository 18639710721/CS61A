# -*- coding: utf-8 -*-
# @Time    : 2022/12/10 14:18
# @Author  : listem
# @FileName: lambda_expressions.py
# @Software: PyCharm


square = lambda x: x * x
print(square)
print(square(5))
print(square(10))

print(lambda x: x * x)
print((lambda x: x * x)(10))


def square(x):
    return x * x


print(square)
