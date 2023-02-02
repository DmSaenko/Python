import game
from loader import dp
from aiogram.types import Message


@dp.message_handler(commands=['start'])
async def mes_start(message: Message):
    for duel in game.total:
        if message.from_user.id == duel[0]:
            await message.answer('Ты уже начал игру! Играй давай!')
            break
    else:
        # game.new_game = True
        await message.answer(f'Привет, {message.from_user.full_name},\n'
                             f'Сыграем в конфеты. У нас есть 150 конфет. Бот Семен и ты берете конфеты по очереди.\n'
                             f'Можно взять от 1 до 28 конфет. Выигрывет тот, кто возьмет последние конфеты на столе.\n'
                             f'Твой ход'\n)
        
        
        my_game = [message.from_user.id, message.from_user.first_name, 150]
        game.total.append(my_game)