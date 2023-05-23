# -*- coding: utf-8 -*-
# @Time    : 2022/1/9 16:01
# @Author  : listem
# @FileName: 04简易计算器.py
# @Software: PyCharm

"""
简易计算器
"""




class easy_compute:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        pass

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        return self.a / self.b    # 带余除法

print("简易计算器")

num1 = int(input("请输入第一个数字"))
num2 = int(input("请输入第二个数字"))

computer = easy_compute(num1,num2)
print("请输入运算: 1, 相加; 2, 相减； 3，相乘； 4， 相除;")


choice = int(input("请输入你的选择 (1/2/3/4)"))
if choice == 1:
    print(computer.add())
elif choice == 2:
    print(computer.subtract())
elif choice == 3:
    print(computer.multiply())
elif choice == 4:
    print(computer.divide())
else:
    print("您输入的类型有错误，请重新输入")
