from aiogram import Bot, Dispatcher, executor, types
from random import *
from environs import Env

env = Env()
env.read_env()

bot_token = env('BOT_TOKEN')

API_TOKEN: str = bot_token

bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher(bot)
answers = ["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова", "Даже не думай",
           "Предрешено", "Вероятнее всего", "Спроси позже", "Мой ответ - нет",
           "Никаких сомнений", "Хорошие перспективы", "Лучше не рассказывать", "По моим данным - нет",
           "Можешь быть уверен в этом", "Да", "Сконцентрируйся и спроси опять", "Весьма сомнительно"]


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.answer('Привет!\nМеня зовут Магический-бот!🔮\n'
                         'Задай мне любой интересующий тебя вопрос и получи ответ')


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.answer(
        'Задай любой вопрос и получишь самый верный и правдивый ответ!\n\n'
        'Обращайся к боту желаний или боту предсказаний в разнообразных ситуациях:\n•Рассудит спорщиков;'
        '\n•Поможет решиться нерешительным;\n•Даст ответ да нет на волнующий запрос;\n•Станет знаком судьбы;'
        '\n•Снимет часть ответственности.\n\nВ одиночестве или в компании, на работе, учебе, в транспорте, '
        'на свадьбе, в магазине - обратись к Боту предсказаний, чтобы получить помощь.\n'
        ' Слушаться решения магического Бота или нет, решать вам.')


@dp.message_handler(content_types=['photo'])
async def send_photo_echo(message: types.Message):
    await message.answer_photo(message.photo[0].file_id)


@dp.message_handler()
async def magic_bot(message: types.Message):
    await message.answer(choice(answers))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
