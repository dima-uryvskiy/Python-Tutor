"""
Условие
По данному натуральному n вычислите сумму 1^3+2^3+3^3+...+n^3.
"""


print(sum([number**3 for number in range(int(input()) + 1)]))
