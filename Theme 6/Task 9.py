"""
Условие
Последовательность состоит из натуральных чисел и завершается числом 0.
Определите индекс наибольшего элемента последовательности.
Если наибольших элементов несколько, выведите индекс первого из них. Нумерация элементов начинается с нуля.
"""


lst = []
value = int(input())
while value != 0:
    lst.append(value)
    value = int(input())
print(lst.index(max(lst)))