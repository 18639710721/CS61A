# -*- coding: utf-8 -*-
# @Time    : 2022/12/13 17:15
# @Author  : listem
# @FileName: c.py
# @Software: PyCharm

# 写一个2*2的矩阵乘法

"""

"""

M1 = [
    [0, 2],
    [1, 0]
]

M2 = [
    [1, -2],
    [1, 0]
]
"""
[
    [2, 0],
    [1, -2]
]
"""
for i in range(len(M1)):
    for j in range(len(M1[i])):
        print(M2[i][j] * M1[i][j] + M2[i+1][j] * M1[i][j + 1])
        print(M2[i][j] * M1[i+1][j] + M2[i+1][j] * M1[i+1][j+1])
        print(M2[i][j+1] * M1[i][j] + M2[i+1][j+1] * M1[i][j+1])
        print(M2[i][j+1] * M1[i+1][j] + M2[i+1][j+1] * M1[i+1][j+1])
        break
    break
