"""
Условие
Даны три целых числа. Выведите значение наименьшего из них.
"""

x, y, c = int(input()), int(input()), int(input())
if y >= x <= c:
    print(x)
elif x >= y <= c:
    print(y)
else:
    print(c)