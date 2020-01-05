"""
Условие
За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m километров?
Программа получает на вход числа n и m.
"""


import math
n, m = int(input()), int(input())
if (m / n).is_integer():
    print(m / n)
elif m < n:
    print(1)
else:
    print(math.ceil(m / n))

