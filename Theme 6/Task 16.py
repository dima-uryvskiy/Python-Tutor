"""
Условие
Дана последовательность натуральных чисел, завершающаяся числом 0.
Определите, какое наибольшее число подряд идущих элементов этой последовательности равны друг другу.
"""


count = 1
max_sequence = -1
value_previous = int(input())
while value_previous != 0:
    value_next = int(input())
    if value_previous == value_next:
        count += 1
    else:
        if max_sequence < count:
            max_sequence = count
        count = 1
    value_previous = value_next
print(max_sequence)