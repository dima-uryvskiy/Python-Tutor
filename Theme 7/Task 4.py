"""
Условие
Дан список чисел. Если в нем есть два соседних элемента одного знака, выведите эти числа.
Если соседних элементов одного знака нет — не выводите ничего.
Если таких пар соседей несколько — выведите первую пару.
"""


lst = list(map(int, input().split()))
for index, value in enumerate(lst):
    if index + 1 != len(lst) and value * lst[index + 1] > 0:
        print(value, lst[index + 1])
        break