"""
Условие
Дан двумерный массив и два числа: i и j. Поменяйте в массиве столбцы с номерами i и j и выведите результат.
Программа получает на вход размеры массива n и m, затем элементы массива, затем числа i и j.
Решение оформите в виде функции swap_columns(a, i, j)
"""


def swap_columns(i, j):
    for index in range(int(n)):
        array[index][i], array[index][j] = array[index][j], array[index][i]


n, m = input().split()
array = [[int(j) for j in input().split()] for i in range(int(n))]
column_one, column_two = input().split()
swap_columns(int(column_one), int(column_two))

for row in array:
    for element in row:
        print(element, end=' ')
    print()
