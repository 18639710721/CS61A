# -*- coding: utf-8 -*-
# @Time    : 2022/12/9 23:57
# @Author  : listem
# @FileName: factorial_falling.py
# @Software: PyCharm

def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"

    # 6 - 3 = 3    6>3  6*5*5
    # 4 - 3 = 1    4>1  4*3*2
    # 4 - 1 = 3    4>3  4
    # 4 - 0 = 4    
    # total, stop = 1, n - k
    # while n > stop:
    #     total, n = total * n, n - 1
    # return total

    # 边界条件 k = 0 直接返回1
    if k == 0:
        return 1
    else:
        return n * falling(n - 1, k - 1)
