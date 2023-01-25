# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11


perem = input('Введите любое число: ')
  
if float(perem) < 0:                           
    perem = float(perem) * -1
     
def sum(perem):                           
    num = 0
    for i in str(perem):
        if i != '.':
            num += int(i)
    return num
   
print(f'Сумма чисел равна {sum(perem)}')