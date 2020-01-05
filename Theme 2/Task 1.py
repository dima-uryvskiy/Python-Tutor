"""
Условие
Даны два целых числа. Выведите значение наименьшего из них.
"""

x, y = int(input()), int(input())
if x > y:
    print(y)
else:
    print(x)