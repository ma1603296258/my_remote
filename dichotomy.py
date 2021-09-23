'''
Author:马俊乾
Date: 2021-09-21 14:58:51
LastEditTime: 2021-09-24 00:45:16
LastEditors: 马俊乾
Description: 二分法求解方程
FilePath: \py\py\dichotomy.py
'''

import math
import numpy as np


def func(x):
    y = math.sin(x)-x/2
    return y


def dichotomy(left, right):
    middle = (left + right)/2
    f0 = func(middle)
    if f0 > 0:
        left = middle
    elif f0 == 0:
        print(middle)
        return 1
    else:
        right = middle
    print(left, right)
    r = right - left
    if r > 0.00000001:
        dichotomy(left, right)
    else:
        print(r)
        return 0


print('left', 'right')
left = np.longdouble(1.5)
right = np.longdouble(2)
dichotomy(left, right)
