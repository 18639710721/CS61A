# -*- coding: utf-8 -*-
# @Time    : 2023/2/15 19:28
# @Author  : listem
# @FileName: express_tree.py
# @Software: PyCharm
"""
Types of expression
    call expression
"""



"""
>>> 2015
2015
>>> 2000 + 15
2015
>>> 1 * 2 * ((3 * 4 * 5 // 6) ** 3) + 7 + 8
2015
>>> # call function
>>> # expression && value
>>> max(2, 4)
4
>>> min(-2, 50000)
-2
>>> # call expression
>>> # 调用表达式
>>> from operator import add,mul
>>> add(2, 3)
5
>>> mul(2, 3)
6
>>> max(1, 2, 3, 4, 5)
5
>>> mul(add(2, mul(4, 6)), add(3, 5))
208
>>> #infix operator 中缀表达式
>>> # Anatomy of a Call expression
>>> # sub expression  operands 操作数  operators 运算符  都是 expression
>>> # nested call expression
>>> # expression tree
>>>
>>>
>>> pi
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    pi
NameError: name 'pi' is not defined
>>> from math import pi
>>> pi
3.141592653589793
>>> pi * 71 / 223 # combination
1.0002380197528042
>>> from math import sin
>>> sin  # bit
<built-in function sin>
>>> sin(pi/2)
1.0
>>> # name
>>> # assignment bind
>>> radius = 10
>>> radius
10
>>> 2 * radius
20
>>> area, circ = pi * radius * radius, 2 * pi * radius
>>> area
314.1592653589793
>>> circ
62.83185307179586
>>> radius = 20
>>> area
314.1592653589793
"""
