"""
Условие
Пирожок в столовой стоит a рублей и b копеек. Определите, сколько рублей и копеек нужно заплатить за n пирожков.
Программа получает на вход три числа: a, b, n, и должна вывести два числа: стоимость покупки в рублях и копейках.
"""


import math
a, b, n = int(input()),  int(input()),  int(input())
number_float = float(a) + float(b / 100)
print(int(math.modf(number_float * n)[1]), int(round(math.modf(number_float * n)[0], 2) * 100), end=" ")

"""
cost = n * (100 * a + b)
print(cost // 100, cost % 100)
"""
