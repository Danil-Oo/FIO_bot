import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters.command import Command

TOKEN = os.getenv('TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO, filename='bot.log',
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


@dp.message(Command(commands=['start']))
async def proccess_command_start(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = (f'Привет, {user_name}! \nНапиши ФИО в кириллице, которое '
            f'ты хочешь конвертировать в латиницу')
    logging.info(f'{user_name} {user_id} запустил бота')
    await bot.send_message(chat_id=user_id, text=text)


@dp.message()
async def send_fio_in_latin(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = message.text
    logging.info(f'{user_name} {user_id} {text}')
    latin_dict = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e',
                  'ё': 'e', 'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'i', 'к': 'k',
                  'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
                  'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts',
                  'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ъ': 'ie', 'ы': 'y',
                  'ь': '', 'э': 'e', 'ю': 'iu', 'я': 'ia'}
    if text.count(' ') != 2:
        await message.answer(text=(f'ФИО должно состоять из 3-х слов, '
                                   f'разделенных одним пробелом'))
        return
    out_str = ''
    for i in text.lower():
        if i in latin_dict:
            out_str += latin_dict[i]
        elif i == ' ':
            out_str += ' '
        else:
            await message.answer(text=(f'ФИО может включать в себя только '
                                       f'буквы в кириллице'))
            return
    await message.answer(text=out_str.title())


if __name__ == '__main__':
    dp.run_polling(bot)
