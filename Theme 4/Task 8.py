"""
Условие
По данному натуральном n вычислите сумму 1!+2!+3!+...+n!.
В решении этой задачи можно использовать только один цикл. Пользоваться математической библиотекой math в этой задаче запрещено
"""


sum_factorial = 0
factorial = 1
for number in range(1, int(input()) + 1):
    factorial *= number
    sum_factorial += factorial
print(sum_factorial)

