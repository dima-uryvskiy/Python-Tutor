"""
Условие
Дано два числа a и b. Выведите гипотенузу треугольника с заданными катетами.
"""


import math
a, b = int(input()), int(input())
gip = math.sqrt(a ** 2 + b ** 2)
print(gip)
