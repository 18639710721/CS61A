# -*- coding: utf-8 -*-
# @Time    : 2022/12/10 19:07
# @Author  : listem
# @FileName: Q1_A_Plus_Abs_B.py
# @Software: PyCharm

# Q1: A Plus Abs B
"""
Python's operator module defines binary functions for Python's intrinsic arithmetic operators.
For example, calling operator.add(2,3) is equivalent to calling the expression 2 + 3; both will return 5.

Note that when the operator module is imported into the namespace,
like at the top of hw01.py, you can just call add(2,3) instead of operator.add(2,3).

Fill in the blanks in the following function for adding a to the absolute value of b,
without calling abs. You may not modify any of the provided code other than the two blanks.
"""
from operator import add, sub


def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    >>> a_plus_abs_b(-1, 4)
    3
    >>> a_plus_abs_b(-1, -4)
    3
    """
    if b < 0:
        f = sub  # a - (- b) = a + b    减去一个负数 等于加上这个数的相反数 即 a + -(-b) = a + b
    else:
        f = add
    return f(a, b)


def two_of_three(i, j, k):
    """Return m*m + n*n, where m and n are the two smallest members of the
    positive numbers i, j, and k.

    >>> two_of_three(1, 2, 3)
    5
    >>> two_of_three(5, 3, 1)
    10
    >>> two_of_three(10, 2, 8)
    68
    >>> two_of_three(5, 5, 5)
    50
    """
    # 枚举所有可能出现的情况 最小的那个便是两个最小的数计算之和
    return min(i ** 2 + j ** 2, i ** 2 + k ** 2, j ** 2 + k ** 2)


def two_of_three2(i, j, k):
    """Return m*m + n*n, where m and n are the two smallest members of the
        positive numbers i, j, and k.

        >>> two_of_three(1, 2, 3)
        5
        >>> two_of_three(5, 3, 1)
        10
        >>> two_of_three(10, 2, 8)
        68
        >>> two_of_three(5, 5, 5)
        50
    """
    # 三个数的xx之和减去最大那个数的xx即可
    return i * i + j * j + k * k - (max(i, j, k) ** 2)


def largest_factor(n):
    """Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    "*** YOUR CODE HERE ***"
    lis = []
    for i in range(1, n):
        if n % i == 0:
            lis.append(i)
    return max(lis)


def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """

    """
    1.Pick a positive integer n as the start.
    2.If n is even, divide it by 2.
    3.If n is odd, multiply it by 3 and add 1.
    4.Continue this process until n is 1.
    """

    "*** YOUR CODE HERE ***"
    print(n)
    counter = 1
    while n != 1:
        if n % 2 == 0:
            n = n // 2
            counter += 1
            print(n)
        else:
            n = n * 3 + 1
            counter += 1
            print(n)
    return counter

