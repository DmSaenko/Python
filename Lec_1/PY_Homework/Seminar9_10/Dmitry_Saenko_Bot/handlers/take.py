import random

from loader import dp
from aiogram.types import Message
import game


@dp.message_handler()
async def mes_help(message: Message):
    for duel in game.total:

        if message.from_user.id == duel[0]:

            count = message.text
            if count.isdigit() and 0 < int(count) < 29:
                duel[2] -= int(count)
                if await check_win(message, 'Ты', duel):
                    return True
                await message.answer(f'{duel[1]} взял {count} конфет и на столе осталось {duel[2]}\n'
                                     f'Теперь ход Семена...')
                bot_take = random.randint(1, 28) if duel[2] > 28 else duel[2]
                duel[2] -= bot_take
                if await check_win(message, 'Семен', duel):
                    return True
                await message.answer(f'Бот Семен взял {bot_take} конфет и '
                                     f'на столе осталось {duel[2]}конфет\n'
                                     f'Давай, ходи...')
            else:
                await message.answer(f'Вводи число от 1 до 28')


async def check_win(message: Message, win: str, duel: list):
    if duel[2] <= 0:
        await message.answer(f'{win} победил! Ну что ж, бывает...')
        game.total.remove(duel)
        return True
    return False
