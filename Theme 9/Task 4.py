"""
Условие
Дано число n. Создайте массив размером n×n и заполните его по следующему правилу.
На главной диагонали должны быть записаны числа 0.
На двух диагоналях, прилегающих к главной, числа 1. На следующих двух диагоналях числа 2, и т.д.
"""


n = int(input())
array = [[0] * n for i in range(n)]

for i in range(n):

    value = 1
    for j in range(i + 1, n):
        array[j][i] = value
        value += 1

    value = 1
    for j in range(i + 1, n):
        array[i][j] = value
        value += 1

for row in array:
    for element in row:
        print(element, end=' ')
    print()
