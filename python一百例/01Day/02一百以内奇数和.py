# -*- coding: utf-8 -*-
# @Time    : 2022/1/8 21:14
# @Author  : listem
# @FileName: 02一百以内奇数和.py
# @Software: PyCharm

"""
求一百以内奇数和
1.用range函数1到100
    如果模2不为0即为奇数     !=
2.用range的步长
    range(1,101,2)   为 1，3，5  即为所有奇数
"""
default_sum = 0
for i in range(101):
    if i % 2 != 0:
        default_sum = default_sum + i

print(default_sum)

num = 0
for i in range(1, 101, 2):
    num += i

print(num)


# 1, 3, 5 等比数列求和公式
num1 = ((1 + 100) * 100) // 2
print(num1)
