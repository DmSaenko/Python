# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов, 
# отличной от 0.
# 
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19



from random import uniform


n = int(input('Введите размер списка '))
my_list = []
for i in range(n):
    f = uniform(0, 9)
    my_list.append(round(f, 2))

min = my_list[0]
max = 0
for i in range(len(my_list)):
    
    if max < my_list[i]:
        max = my_list[i]
    if min > my_list[i]:
        min = my_list[i]
dif = (max - int(max)) - (min - int(min))

print(f'Список: {my_list}')
print(f'Максимальное число: {max}\nМинимальное число: {min}')
print(f'Разница между min и maх значениями дробной части:  {round(dif,2)}')