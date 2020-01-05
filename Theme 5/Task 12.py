"""
Условие
Дана строка. Удалите из нее все символы, чьи индексы делятся на 3.
"""


s = input()
for index, symbol in enumerate(s):
    if index % 3 == 0:
        continue
    else:
        print(symbol, end="")