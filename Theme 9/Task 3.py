"""
Условие
Даны два числа n и m.
Создайте двумерный массив размером n×m и заполните его символами "." и "*" в шахматном порядке.
В левом верхнем углу должна стоять точка.
"""


def add_element(start):
    for j in range(start, int(m), 2):
        array[i][j] = '*'


n, m = input().split()
array = [['.'] * int(m) for i in range(int(n))]

for i in range(int(n)):
    if i % 2 == 0:
        add_element(1)
    else:
        add_element(0)

for row in array:
    for element in row:
        print(element, end=' ')
    print()

