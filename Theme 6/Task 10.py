"""
Условие
Определите количество четных элементов в последовательности, завершающейся числом 0.
"""


count = 0
value = int(input())
while value != 0:
    if value % 2 == 0:
        count += 1
    value = int(input())
print(count)