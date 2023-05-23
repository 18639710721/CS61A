# -*- coding: utf-8 -*-
# @Time    : 2023/2/15 3:31
# @Author  : listem
# @FileName: garbage.py
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


import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as image

# from warping import *
from numpy import  linalg as la
from IPython.display import  clear_output

# load and display an image
# img = plt.imread()   # load image
# plt.figure(figsize=(size[0]/72), size[1]/72)