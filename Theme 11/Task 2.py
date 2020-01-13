"""
Условие
Вам дан словарь, состоящий из пар слов. Каждое слово является синонимом к парному ему слову.
Все слова в словаре различны.
Для слова из словаря, записанного в последней строке, определите его синоним.
"""


dict_word = dict()

for value in range(int(input())):
    first_word, second_word = input().split()
    dict_word[first_word] = second_word

word = input()

for key, value in dict_word.items():
    if value == word:
        print(key)
    elif key == word:
        print(value)

