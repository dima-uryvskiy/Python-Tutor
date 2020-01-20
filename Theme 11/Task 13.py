"""
Условие
В генеалогическом древе определите для двух элементов их наименьшего общего предка (Lowest Common Ancestor).
Наименьшим общим предком элементов A и B является такой элемент C, что С является предком A, C является предком B, при
этом глубина C является наибольшей из возможных. При этом элемент считается своим собственным предком.
Формат входных данных аналогичен предыдущей задаче
Для каждого запроса выведите наименьшего общего предка данных элементов.
"""


def find_parent(parent):
    if parent is None:
        return
    else:
        lst_parent.append(parent)
        return find_parent(dict_family[parent])


def find_family(child):
    if child in lst_parent or people_fist in lst_parent:
        return child
    else:
        return find_family(dict_family[child])


lst_parent = []
dict_family = {}
for i in range(int(input()) - 1):
    name_child, name_parent = input().split()
    dict_family[name_child] = name_parent
    if name_parent not in dict_family.keys():  # если нет потомков
        dict_family[name_parent] = None

for j in range(int(input())):
    people_fist, people_second = input().split()
    find_parent(people_second)
    print(find_family(people_fist))
    lst_parent.clear()


