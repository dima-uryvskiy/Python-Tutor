"""
Условие
Выведите все четные элементы списка. При этом используйте цикл for, перебирающий элементы списка, а не их индексы!
"""


lst = list(map(int, input().split()))
for number in lst:
    if number % 2 == 0:
        print(number)