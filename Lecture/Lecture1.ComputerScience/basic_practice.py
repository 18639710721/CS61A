# -*- coding: utf-8 -*-
# @Time    : 2023/2/14 16:41
# @Author  : listem
# @FileName: test2.py
# @Software: PyCharm

"""
change the mapping of pixel value to colro
改变像素值和颜色的映射
    颜色变换

扭曲图像
车牌识别
    射影几何

fried
distort
bank robber
slide
accurate
lecture hall


不要被想象力和技能限制,享受思考的乐趣
"""
# request Download
# 用来下载莎士比亚的txt
# import requests
#
# shakespeare = requests.get('http://composingprograms.com/shakespeare.txt')
# print(shakespeare.text)
# with open("shakespeare.txt", "w") as f:
#     f.write(shakespeare.text)

# with open("shakespeare.txt", "r+") as r:
#     print(r.read())

# Numeric expressions
"""
>>> 2020
2020
>>> 2000 + 20
2020
>>> -1 + 2 + 3 + 4 * ((5 // 6) + 7 * 8 * 9)
2020
>>> abs(-2)
2
>>> abs(2301 - 4321)
2020
>>> "Go Bears"
'Go Bears'
>>> 'God' + 'ears'
'Godears'
"""

# Objects
shakes = open("shakespeare.txt")
# Wrapper是调度器的意思
print(shakes)  # <_io.TextIOWrapper name='shakespeare.txt' mode='r' encoding='cp936'>
text = shakes.read().split()  # 默认按空格划分成字符串
print(len(text))  # 980637
print(text[:25])  # 前25个单词
print(text.count("the"))  # 23272
print(text.count("thou"))
print(text.count("you"))
print(text.count("forsooth"))
print(text.count(","))
print(text.count(",") / len(text))  # %0.08都是逗号 0.0834427010198473

# Sets
words = set(text)  # 利用set元素的唯一性去重
print(len(words))  # 33505
print("forsooth" in words)  # True
print("computer" in words)  # False  计算机不存在于莎士比亚的时代
print("John" in words)  # True
print(text.count("John"))  # 263
print(text.count("Hany"))  # 0

# Combinations
print("draw"[0])
# 发现有大小写和一些标点符号
print({w[0] for w in words})  # 获得每个letters的第一个字母并去重
print(text.count("egg"))
print(len({w[0] for w in words}))  # 71


#Data
print("draw"[::-1])  # backwards  ward
print({w for w in words if w == w[::-1]})  # 单词和它的反转都一样
print({w for w in words if w == w[::-1] and len(w) > 4})  # 并且长度大于4
print({w for w in words if w[::-1] in words and len(w) == 4})  # 如果反转后的词在去重的单词里面并且长度等于4
print({w for w in words if w[::-1] in words and len(w) == 5})
print({w for w in words if w[::-1] in words and len(w) == 6})
print({w for w in words if w[::-1] in words and len(w) > 6})  # set() 没有大于6的



