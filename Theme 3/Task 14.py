"""
Условие
С начала суток часовая стрелка повернулась на угол в α градусов.
Определите на какой угол повернулась минутная стрелка с начала последнего часа.
Входные и выходные данные — действительные числа.
"""


alpha = float(input())
print(alpha % 30 * 12)
