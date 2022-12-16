# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import os
os.system('cls')

ax = float(input('Введите координаты точки A по оси x:  '))
ay = float(input('Введите координаты точки A по оси y:  '))
bx = float(input('Введите координаты точки B по оси x:  '))
by = float(input('Введите координаты точки B по оси y:  '))

import math

distance= math.sqrt((ax-bx)**2+(ay-by)**2)

print (f'Точка А: {ax, ay}' )
print (f'Точка B: {bx, by}' )

print(f'Растояние от точки A до точки B = {distance}' )
#     print('{:.3f}'.format(a), sep='')