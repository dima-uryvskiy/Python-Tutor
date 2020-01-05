"""
Условие
Даны четыре действительных числа: x1, y1, x2, y2. Напишите функцию distance(x1, y1, x2, y2),
вычисляющая расстояние между точкой (x1,y1) и (x2,y2).
Считайте четыре действительных числа и выведите результат работы этой функции.
Если вы не знаете, как решить эту задачу, то вы, возможно, не изучали в школе теорему Пифагора.
Попробуйте прочитать о ней на Википедии.
"""


import math


def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


print(distance(float(input()), float(input()), float(input()), float(input())))