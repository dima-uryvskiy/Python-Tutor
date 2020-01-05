"""
Условие
Определите среднее значение всех элементов последовательности, завершающейся числом 0.
"""


sum_input = 0
count = 0
value = int(input())
while value != 0:
    sum_input += value
    count += 1
    value = int(input())
print(sum_input / count)