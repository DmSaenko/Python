from loader import dp
from aiogram.types import Message


@dp.message_handler(commands=['help'])
async def mes_help(message: Message):
    await message.answer(f'Есть проблемы?')
    print(message.from_user.id)