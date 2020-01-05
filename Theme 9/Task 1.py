"""
Условие
Найдите индексы первого вхождения максимального элемента.
Выведите два числа: номер строки и номер столбца, в которых стоит наибольший элемент в двумерном массиве.
Если таких элементов несколько, то выводится тот, у которого меньше номер строки, а если номера строк равны то тот,
у которого меньше номер столбца.
Программа получает на вход размеры массива n и m, затем n строк по m чисел в каждой.
"""


n, m = input().split()

array = [[int(j) for j in input().split()] for i in range(int(n))]
max_array, i_element, j_element = array[0][0], 0, 0

for i in range(int(n)):
    for j in range(int(m)):
        if max_array < array[i][j]:
            max_array = array[i][j]
            i_element, j_element = i, j

print(i_element, j_element, end=' ')
