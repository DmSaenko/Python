"""Задайте список из нескольких чисел. Напишите программу,
которая найдёт сумму элементов списка, стоящих на позиции с нечетным индексом.
Пример:
[2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12 """

from random import randint as RI


my_list = [RI(0, 100) for i in range(8)]
print(f'Список полный: {my_list}')
my_list = list(filter(lambda i: i % 2 != 0, my_list)) 
summa = sum(i for i in my_list)
print(f'Список нечетных: {my_list}')

print(f'Сумма нечетных чисел равна: {summa}')