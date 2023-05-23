# -*- coding: utf-8 -*-
# @Time    : 2022/1/9 21:57
# @Author  : listem
# @FileName: eatSnake.py
# @Software: PyCharm


"""
面向对象
    蛇
        属性
            1.初始化长度
            2.初始化投部指向的方向
        行为
            1.吃
            2.死亡
                撞墙死亡
                首尾相接死亡
            3.移动
            4.方向
    食物




"""
import sys        # 键盘的操作
import random     # 食物是随机产生的
import pygame
class Snake(object):
    def __init__(self):
        self.direction = pygame.K_RIGHT # 初始化默认是向右走
        self.body = []                  # 蛇身的长度是一个列表

    def addnode(self):
        if self.body:
            pass







# 全局变量
SCREEN_X = 600
SCREEN_Y = 600


def main():
    pygame.init()
    screen_size = (SCREEN_X,SCREEN_Y)
    pygame.display.set_mode(screen_size)
    pygame.display.set_caption("贪吃蛇")
    clock = pygame.time.Clock()
    scores = 0   # 定义成绩
    isdead = False   # 判断是否死亡



main()











"""
教程地址
    https://www.bilibili.com/video/BV1Q7411C7Cq?from=search&seid=12342197733567482924&spm_id_from=333.337.0.0
"""