''' Создайте программу для игры с конфетами человек против человека.
Условие задачи: На столе лежит заданное количество конфет. Играют два игрока делая ход друг после друга.
Первый ход определяется жеребьёвкой.
За один ход можно забрать не более чем 28 конфет.
Все конфеты оппонента достаются сделавшему последний ход.
a) Добавьте игру против бота
b) Подумайте как наделить бота "интеллектом"  '''

from random import randint as RI

greetings = ('Привет, давай поиграем в игру под название - "Конфеты"!\n'
             'Правила игры:\n'
             'Напишите сколько конфет вы хотите разыграть.\n'
             'Играют два игрока делая ход друг после друга,\n'
             'но если в поле второй игрок ввести слово - бот, игра будет с компьютером.\n'
             'За один ход можно забрать не более чем 28 конфет.\n'
             'Все конфеты оппонента достаются сделавшему последний ход.')
print(greetings)


def player_vs_player(player_1, player_2):
    all_sweets = int(input('Введите количество конфет которые хотите разыграть: '))
    max_move = 28
    count = 0
    print(f'А теперь {player_1} и {player_2} поиграем!')
    print('Кидаем монетку и .....')

    draw = RI(1, 2)
    if draw == 1:
        eagle = player_1
        tails = player_2
    else:
        eagle = player_2
        tails = player_1
    print(f'Поздравляю {eagle} ты ходишь первым !')

    while all_sweets > 0:
        if count == 0:
            move = int(input(f'\nТвой ход, {eagle}: '))
            while True:
                try:
                    if move > all_sweets or move > max_move:
                        move = int(input(
                            f'Можно взять только {max_move} конфет или не больше остатка\n'
                            f'{eagle}, попробуй еще раз: '))
                    else:
                        all_sweets = all_sweets - move
                        break
                except:
                    print('Зачем вводишь буквы? А?')
        if all_sweets > 0:
            print(f'\nОсталось: {all_sweets}')
            count = 1
        else:
            print('Конфеты кончились\nА это значит что: ')
            break

        if count == 1:
            move = int(input(f'\nТвой ход, {tails}: '))
            while True:
                try:
                    if move > all_sweets or move > max_move:
                        move = int(input(
                            f'Можно взять только {max_move} конфет или не больше остатка\n'
                            f'{tails}, попробуй еще раз: '))
                    else:
                        all_sweets = all_sweets - move
                        break
                except:
                    print('Зачем вводишь буквы? А?')

        if all_sweets > 0:
            print(f'\nОсталось: {all_sweets}')
            count = 0
        else:
            print('Конфеты кончились\nА это значит что: ')
            break

    if count == 1:
        print(f'{tails} ПОБЕДИЛ!!!')
    if count == 0:
        print(f'{eagle} ПОБЕДИЛ!!!')


def player_vs_bot(player_1, player_2):
    all_sweets = int(input('Введите количество конфет которые хотите разыграть: '))
    max_move = 28
    count = 0
    players = [player_1, player_2]
    print(f'А теперь {player_1} и {player_2} поиграем!')
    print('Кидаем монетку и .....')

    draw = RI(-1, 0)

    print(f'Поздравляю {players[draw + 1]} ты ходишь первым !')

    while all_sweets > 0:
        draw += 1
        if players[draw % 2] == 'Бот':
            move = f'\nХодит, {players[draw % 2]}:'
            print(move, end=' ')
            if all_sweets % (1 + max_move) != 0:
                move = all_sweets % (1 + max_move)
                print(move)
            else:
                move = RI(1, max_move)
                print(move)
            all_sweets = all_sweets - move
            if all_sweets > 0:
                print(f'\nОсталось: {all_sweets}')
            else:
                print('Конфеты кончились\nА это значит что: ')
                break

        else:
            move = int(input(f'\nТвой ход, {players[draw % 2]}: '))
            while True:
                try:
                    if move > all_sweets or move > max_move:
                        move = int(input(
                            f'Можно взять только {max_move} конфет или не больше остатка\n'
                            f'{players[draw % 2]}, попробуй еще раз: '))
                    else:
                        all_sweets = all_sweets - move
                        break
                except:
                    print('Зачем вводишь буквы? А?')
            if all_sweets > 0:
                print(f'\nОсталось: {all_sweets}')
            else:
                print('Конфеты кончились\nА это значит что: ')

    print(f'{players[draw % 2]} ПОБЕДИЛ!!!')


def game_selection():
    player_1 = input('\nИгрок номер 1: ')
    player_2 = input('\nИгрок номер 2: ')
    if player_2 == 'Бот':
        player_vs_bot(player_1, player_2)
    else:
        player_vs_player(player_1, player_2)


game_selection()