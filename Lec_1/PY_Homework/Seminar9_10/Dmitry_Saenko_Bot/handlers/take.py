from loader import dp
from aiogram.types import Message
from game import total
from random import randint as RI


@dp.message_handler()
async def mes_help(message: Message):
    if message.from_user.id in total:
        if message.text.isdigit() and 0 < int(message.text) < 29:
            total[message.from_user.id] -= int(message.text)
            
            if total[message.from_user.id] <= 0:
                await message.answer('You Win!!')
                total.pop(message.from_user.id)
            else:
                await message.answer(f'Остается {total[message.from_user.id]}')
                num = RI(1, 28)
                total[message.from_user.id] -= num
                await message.answer(f'Семен взял {num}, осталось {total[message.from_user.id]}')
                if total[message.from_user.id] <= 0:
                    await message.answer('You Lose!!')
                    total.pop(message.from_user.id)
        else:
            await message.answer(f'Не понял, повтори')
    else:
        await message.answer("Чтобы играть жми /start")
