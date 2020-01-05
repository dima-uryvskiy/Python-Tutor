"""
Условие
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 — координаты 8 ферзей.
Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.
"""


lst_one = []
lst_two = []
for i in range(8):
    new_x, new_y = [int(s) for s in input().split()]
    lst_one.append(new_x)
    lst_two.append(new_y)

result = False
for i in range(8):
    for j in range(i + 1, 8):
        if lst_one[i] == lst_one[j] or lst_two[i] == lst_two[j] or abs(lst_one[i] - lst_one[j]) == abs(lst_two[i] - lst_two[j]):
            result = True

if result:
    print('YES')
else:
    print('NO')



