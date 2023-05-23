# -*- coding: utf-8 -*-
# @Time    : 2022/12/21 16:21
# @Author  : listem
# @FileName: test1.py
# @Software: PyCharm

from typing import *


def quick_sort(items: List[int]) -> List[int]:
    pivot = items[0]
    low = 0
    high = len(items) - 1

    while low < high:
        while low < high and items[pivot] <= items[high]:
            low = low + 1
