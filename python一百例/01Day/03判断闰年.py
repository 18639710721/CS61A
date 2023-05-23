# -*- coding: utf-8 -*-
# @Time    : 2022/1/8 21:22
# @Author  : listem
# @FileName: 03判断闰年.py
# @Software: PyCharm
"""
普通闰年
    公历年份是4的倍数不是一百的倍数的普通闰年
世纪闰年
    公历年份是整百倍数 必须是四百的倍数才是世纪闰年

普通闰年
    能够倍4整除，不能被100整除
世纪闰年
    能倍400整除
"""

year = int(input("请输入年份"))
if year % 4 == 0:
    if year % 400 == 0:
        print("是世纪闰年")
    else:
        print("是普通闰年")
else:
    print("不是闰年")