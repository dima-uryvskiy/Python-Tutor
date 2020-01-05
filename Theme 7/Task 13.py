"""
Условие
Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
"""


lst = input().split()
count = 0
for index, value in enumerate(lst):
    for next_value in lst[index + 1: len(lst)]:
        if value == next_value:
            count += 1
print(count)