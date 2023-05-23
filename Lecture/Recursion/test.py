# -*- coding: utf-8 -*-
# @Time    : 2022/12/14 17:56
# @Author  : listem
# @FileName: test.py
# @Software: PyCharm



test_str = ""


def turing_machine(test_str):
    lis = list(test_str)
    lis.append("#")
    lis.insert(0, "#")

    print("".join(lis))


turing_machine("33")
