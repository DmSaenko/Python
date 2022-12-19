# 2. Для натурального n создать словарь ключ-значение,
# состоящий из элементов последовательности 3n + 1.

# Пример:
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}



# var 1

n = int(input('Введите n: '))

my_dict = {}

for key in range(1, n+1):

    my_dict[key] = 3 * key * 1
    
print(my_dict)
    


# my_dict = {}


# for key, range item in my_dict.items()

