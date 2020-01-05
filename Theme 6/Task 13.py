"""
Условие
Последовательность состоит из натуральных чисел и завершается числом 0.
Определите, сколько элементов этой последовательности равны ее наибольшему элементу.
"""


lst = []
value = int(input())
while value != 0:
    lst.append(str(value))
    value = int(input())

max_element = max(lst)
print(" ".join(lst).count(str(max_element)))