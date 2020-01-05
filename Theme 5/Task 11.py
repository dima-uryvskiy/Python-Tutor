"""
Условие
Дана строка. Замените в этой строке все появления буквы h на букву H, кроме первого и последнего вхождения.
"""


s = input()
part_begin = s[:s.find('h') + 1]
part_mind = s[s.find('h') + 1:s.rfind('h')]
part_end = s[s.rfind('h'):]
print(part_begin + part_mind.replace('h', 'H') + part_end)

