# -*- coding: utf-8 -*-
# @Time    : 2022/1/9 16:23
# @Author  : listem
# @FileName:
# @Software: PyCharm

from random import randint

"""
猜数字游戏
    guess(start,end,)
    二分法
    log
"""
print("这是一个猜数字游戏，输入1到100的整数，但只有五次机会")


def guess(start, end, times):
    value = randint(start, end)  # 随机生成一个1到100以内的整数

    for i in range(times):
        prompt = "开始猜吧，请输入一个整数"

        try:
            guessNum = int(input(prompt))
            if guessNum == value:
                print("猜对了，但也没有奖励")
                break
            else:
                if guessNum > value:
                    print("猜大了")
                else:
                    print("猜小了")
        except:
            print("请输入整数")

    else:
        print("很遗憾，游戏结束")
        print(f"数字的值为{value}")


if __name__ == '__main__':
    guess(1, 100, 5)
