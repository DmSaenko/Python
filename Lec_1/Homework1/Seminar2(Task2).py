# Задайте список из n чисел последовательности (1 + 1/n)**n, выведите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06


# var 1

# number = int(input('Введите число: '))


# res = [round((1 + 1/i)**i, 2) for i in range(1, number+1)]
    
    
# print(f'Для n = {number} Последовательность:{res} \nСумма: {round(sum(res), 2)}')

# var 2


number = int(input('Введите число: '))

my_list = [] 

for i in range(1, number+1):
    my_list.append((1 + 1/i)**i)    

formatted_list = [round(item, 2) for item in my_list]
    
print(f'Для n = {number} Последовательность:{formatted_list}')  
  
print(f'Сумма: {round(sum(my_list), 2)}')