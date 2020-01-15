"""
Условие
Дан текст: в первой строке задано число строк, далее идут сами строки.
Выведите слово, которое в этом тексте встречается чаще всего. Если таких слов несколько, выведите то,
которое меньше в лексикографическом порядке.
"""


dict_word = {}
for i in range(int(input())):
    string = input()
    for word in string.split():
        dict_word[word] = dict_word.get(word, 0) + 1

for key, value in sorted(dict_word.items()):
    if value >= max(dict_word.values()) and key <= max(dict_word.keys()):
        print(key)
        break
