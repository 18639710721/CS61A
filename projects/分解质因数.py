# -*- coding: utf-8 -*-
# @Time    : 2022/12/8 12:59
# @Author  : listem
# @FileName: 分解质因数.py
# @Software: PyCharm

def prime_factors(n):
    """Print the prime factors of n in non-decreasing order

    >>> prime_factors(8)
    2
    2
    2
    >>> prime_factors(9)
    3
    3
    >>> prime_factors(10)
    2
    5
    >>> prime_factors(11)
    11
    >>> prime_factors(858)
    2
    3
    11
    13
    """
    while n > 1:
        min_num = smallest_prime_factor(n)  # 找到最小的那个公因数
        n = n // min_num  # 使用 floor除法 缩小n的范围
        print(min_num)


# 递增的序列实现返回一个最小公因数
def smallest_prime_factor(n):
    k = 2  # 从2开始
    # 跳出while的条件是n % k == 0 即这n能被k整除 k是n的公因数
    while n % k != 0:  # 一旦为False 跳出 while
        k = k + 1
    return k  # 一旦能被整除 即返回公因数k


# prime_factors(15)


# V2版本 复杂了
# ctrl + r 替换变量名
def prime_factors_unreadable(n):
    """Print the prime factors of n in non-decreasing order

    >>> prime_factors_unreadable(8)
    2
    2
    2
    >>> prime_factors_unreadable(9)
    3
    3
    >>> prime_factors_unreadable(10)
    2
    5
    >>> prime_factors_unreadable(11)
    11
    >>> prime_factors_unreadable(858)
    2
    3
    11
    13
    """
    while n > 1:
        # 这里把提供最小公因数的函数换成了这一部分代码  只要能模n整除就继续除下去
        min_num = 2
        while n % min_num != 0:
            min_num = min_num + 1

        n = n // min_num  # 使用 floor除法 缩小n的范围
        print(min_num)


# prime_factors_unreadable(3)

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
