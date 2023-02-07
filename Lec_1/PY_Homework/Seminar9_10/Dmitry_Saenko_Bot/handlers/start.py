from loader import dp
from aiogram.types import Message
from game import max_total, total
from random import randint as RI


@dp.message_handler(commands=['start'])
async def mes_start(message: Message):

    candy = max_total
    if len(message.text) > 6:
        candy = message.text[6:].replace(' ', '')
    total[message.from_user.id] = candy
    await message.answer(f'Привет, {message.from_user.full_name} Сыграем в конфеты. У нас есть {total[message.from_user.id]} конфет\nБот Семен и ты берете конфеты по очереди \nМожно взять от 1 до 28 конфет. Выигрывет тот, кто возьмет последние конфеты на столе')

    dispute = RI(0,1)

    if dispute:
        await message.answer(f'Твой ход!')
    else:
        num = RI(1, 28)
        total[message.from_user.id] -= num
        await message.answer(f'Первый ход за Cеменом!\n Семен взял {num}, осталось {total[message.from_user.id]}')
        await message.answer(f'Твой ход')

