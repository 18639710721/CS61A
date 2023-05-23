# -*- coding: utf-8 -*-
# @Time    : 2022/12/11 13:12
# @Author  : listem
# @FileName: recursive_functions.py
# @Software: PyCharm

"""
Recursive Functions
    Definition: A function is called recursive if the body of that
    function calls itself, either directly or indirectly

    Implication: Executing the body of a recursive function may require
    applying that function again.

    Sierpinski Triangle 谢尔宾斯三角形
        自相似
    数字求和
"""


# 递归实现 1-100求和
def num_sums(n: int):
    if n == 1:
        return 1
    else:
        return n + num_sums(n - 1)


print(num_sums(100))
