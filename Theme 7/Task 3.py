"""
Условие
Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.
"""


lst = list(map(int, input().split()))
for index, value in enumerate(lst):
    if index + 1 != len(lst) and lst[index + 1] > value:
        print(lst[index + 1])