"""
Условие
Во входной строке записана последовательность чисел через пробел.
Для каждого числа выведите слово YES (в отдельной строке), если это число ранее встречалось в последовательности или
NO, если не встречалось.
"""


result_set = set()

for value in input().split():
    if value in result_set:
        print('YES')
    else:
        print('NO')
        result_set.add(value)
