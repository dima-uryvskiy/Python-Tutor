"""
Условие
Даны два целых числа A и B (при этом A ≤ B). Выведите все числа от A до B включительно.
"""


a, b = int(input()),  int(input())
for number in range(a, b + 1):
    print(number)
