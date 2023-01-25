
"""Реализуйте алгоритм перемешивания списка.
НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE,
максимум использование библиотеки Random для и получения случайного int"""


from random import randint as RI

my_list = [RI(0, 100) for i in range(8)]
print(f'Список: {my_list}')

def perem_list():
    global my_list
    for i in range(len(my_list) - 1, 0, -1):
        j = RI(0, i + 1)
        my_list[i], my_list[j] = my_list[j], my_list[i]
    return my_list

my_list_list = perem_list()
print(f'Перемешенный список: {my_list}')

