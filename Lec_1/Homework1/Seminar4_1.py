# a*x**2 + b*x + c = 0

import math

my_str = '3*x**2 - 12*x + 6 = 0'
# a1 = my_str.split()
a2 = my_str.replace(' ', '').replace('-', '+-').replace('=0', '').replace('**2', '').replace('*', '').replace('x', '').split('+')


a = int(a2[0])
b = int(a2[1])
c = int(a2[2])

discr = b ** 2 - 4 * a * c
print("Дискриминант D = %.2f" % discr)

if discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
elif discr == 0:
    x = -b / (2 * a)
    print("x = %.2f" % x)
else:
    print("Корней нет")
