"""
Условие
Дан список стран и городов каждой страны. Затем даны названия городов.
Для каждого города укажите, в какой стране он находится.
"""


dict_country = {}
for i in range(int(input())):
    country, *city = input().split()
    dict_country[country] = city

for j in range(int(input())):
    town = input()
    for key, value in dict_country.items():
        if town in value:
            print(key)