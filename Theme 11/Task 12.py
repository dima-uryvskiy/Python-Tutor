"""
Условие
Даны два элемента в дереве. Определите, является ли один из них потомком другого.
Во входных данных записано дерево в том же формате, что и в предыдущей задаче Далее идет число запросов K.
В каждой из следующих K строк, содержатся имена двух элементов дерева.
Для каждого такого запроса выведите одно из трех чисел: 1, если первый элемент является предком второго, 2, если второй
является предком первого или 0, если ни один из них не является предком другого.
"""


def find_family(child, parent):
    if child is None:
        return False
    elif child == parent:
        return True
    else:
        return find_family(dict_family[child], parent)


dict_family = {}
for i in range(int(input()) - 1):
    name_child, name_parent = input().split()
    dict_family[name_child] = name_parent
    if name_parent not in dict_family.keys():  # если нет потомков
        dict_family[name_parent] = None

for j in range(int(input())):
    people_fist, people_second = input().split()
    if find_family(people_fist, people_second):
        print(2, end=' ')
    elif find_family(people_second, people_fist):
        print(1, end=' ')
    else:
        print(0, end=' ')
