"""
Условие
В списке все элементы различны. Поменяйте местами минимальный и максимальный элемент этого списка.
"""


lst = [int(i) for i in input().split()]
index_max = lst.index(max(lst))
index_min = lst.index(min(lst))
lst[index_max], lst[index_min] = lst[index_min], lst[index_max]
print(*lst)