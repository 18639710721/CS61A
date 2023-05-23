# -*- coding: utf-8 -*-
# @Time    : 2022/12/10 22:20
# @Author  : listem
# @FileName: self_reference.py
# @Software: PyCharm

def print_all(x: int):
    print(x)
    return print_all    # 每次返回的都是函数的reference


print_all(3)(4)(5)


# 将参数累计相加
def print_sum(x):
    print(x)

    def next_num(y):
        print(y)
        return print_sum(x + y)

    return next_num


print_sum(1)(3)(5)
