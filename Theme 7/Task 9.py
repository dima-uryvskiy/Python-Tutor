"""
Условие
Переставьте соседние элементы списка (A[0] c A[1], A[2] c A[3] и т. д.).
Если элементов нечетное число, то последний элемент остается на своем месте.
"""


lst = input().split()
index = 0
while index < len(lst):
    if len(lst) != index + 1:
        lst[index], lst[index + 1] = lst[index + 1], lst[index]
    index += 2
print(*lst)