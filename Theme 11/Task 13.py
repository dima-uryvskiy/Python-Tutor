"""
Условие
В генеалогическом древе определите для двух элементов их наименьшего общего предка (Lowest Common Ancestor).
Наименьшим общим предком элементов A и B является такой элемент C, что С является предком A, C является предком B, при
этом глубина C является наибольшей из возможных. При этом элемент считается своим собственным предком.
Формат входных данных аналогичен предыдущей задаче
Для каждого запроса выведите наименьшего общего предка данных элементов.
"""


def find_family(child, parent):
    if child == parent or child == people_second:
        return child
    elif parent == people_fist:
        return parent
    elif dict_family[child] is None and parent is not None:
        return find_family(child, dict_family[parent])
    elif child is not None and dict_family[parent] is None:
        return find_family(dict_family[child], parent)
    elif child is None or parent is None:
        return
    else:
        return find_family(dict_family[child], dict_family[parent])


dict_family = {}
for i in range(int(input()) - 1):
    name_child, name_parent = input().split()
    dict_family[name_child] = name_parent
    if name_parent not in dict_family.keys():  # если нет потомков
        dict_family[name_parent] = None

for j in range(int(input())):
    people_fist, people_second = input().split()
    print(find_family(people_fist, people_second))
