# 1.Вычислить число c заданной точностью d

# *Пример:*

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$


# from math import log10 as log
# from math import pi


# def number(x): return int(log(1/float(x)))


# a = round(pi, number(float(input("Введите точноть округление"))))


# print(a)

from math import log10 as log
from math import pi


def number(x): return int(log(1/float(x)))


a = round(pi, number(float(input("Введите точноть округление"))))


print(a)
