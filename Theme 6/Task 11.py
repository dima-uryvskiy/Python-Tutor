"""
Условие
Последовательность состоит из натуральных чисел и завершается числом 0.
Определите, сколько элементов этой последовательности больше предыдущего элемента.
"""


count = 0
value_previous = int(input())
while value_previous != 0:
    value_next = int(input())
    if value_previous < value_next:
        count += 1
    value_previous = value_next
print(count)