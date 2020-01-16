"""
Условие
Дана база данных о продажах некоторого интернет-магазина.
Каждая строка входного файла представляет собой запись вида Покупатель товар количество, где Покупатель — имя покупателя
(строка без пробелов), товар — название товара (строка без пробелов),
количество — количество приобретенных единиц товара.
Создайте список всех покупателей, а для каждого покупателя подсчитайте количество приобретенных им единиц каждого вида
товаров. Список покупателей, а также список товаров для каждого покупателя нужно выводить в лексикографическом порядке.
"""


#  для прохождения тестов на сайте
import sys


dict_result = {}
for line in sys.stdin.readlines():
    person, product, price = line.split()
    dict_result[person] = dict_result.get(person, {product: 0})
    dict_result[person][product] = dict_result[person].get(product, 0) + int(price)

for person, value in dict_result.items():
    print(person + ':')
    for key, element in sorted(value.items()):
        print(key, element)


#  для тестирования в PyCharm
"""
dict_result = {}
line = input()
while line != '':
    person, product, price = line.split()
    dict_result[person] = dict_result.get(person, {product: 0})
    dict_result[person][product] = dict_result[person].get(product, 0) + int(price)
    line = input()

for person, value in dict_result.items():
    print(person + ':')
    for key, element in sorted(value.items()):
        print(key, element)
"""




