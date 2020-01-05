"""
Условие
Дан список чисел. Определите, сколько в этом списке элементов, к
оторые больше двух своих соседей, и выведите количество таких элементов.
Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
"""


lst = [int(i) for i in input().split()]
count = 0
for index, value in enumerate(lst):
    if index + 1 != len(lst) and index != 0 and lst[index - 1] < value > lst[index + 1]:
        count += 1
print(count)