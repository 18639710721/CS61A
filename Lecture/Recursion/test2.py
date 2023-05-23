# -*- coding: utf-8 -*-
# @Time    : 2022/12/27 15:18
# @Author  : listem
# @FileName: test2.py
# @Software: PyCharm

from typing import *
import random


def bubble_sort(item: List[int]) -> List[int]:
    for i in range(len(item) - 1):
        for j in range(len(item) - 1 - i):
            if item[j] > item[j+1]:
                item[j], item[j+1] = item[j+1], item[j]
    return item


test_set = [random.randint(1, 100) for i in range(10)]
print(test_set)
print(bubble_sort(test_set))
