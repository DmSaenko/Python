# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

my_list=["djfhd74hd", "77", "df8fg8fvj","fjf7776ff7"]

numb = input("Введите число: ")

for i in range(len(my_list)):
    
    if  numb in my_list[i]:
        
        print(f"Число {numb} есть в строке{my_list[i]} у которой индекс{i}")
        break
else:

    print(f'В заданном списке нет вхождения {numb}')

