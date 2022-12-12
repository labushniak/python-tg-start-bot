from asyncio.log import logger
from distutils.cmd import Command
from aiogram import Bot, Dispatcher, types
import asyncio
import logging

from aiogram.filters import Filter
from aiogram import F

from aiogram.types import BotCommand, BotCommandScopeDefault
from aiogram.filters import Text

token = '5787754570:AAHlfyva3GAjXInHuVVe53C5foLDYb0o_W8'

admin_id = 378019212

logger = logging.getLogger(__name__)

async def comm(bot: Bot):
    command = [
        BotCommand(
            command = 'start',
            description = 'Начало работы',
        ),
        BotCommand(
            command = 'help',
            description = 'Помощь',
        ),
    ]

    await bot.set_my_commands(command, BotCommandScopeDefault())

async def start_up(bot:Bot):
    await comm(bot)
    await bot.send_message(admin_id, text="Бот запущен!")

async def sd(bot:Bot):
    await bot.send_message(admin_id, text="Бот выключен.")

async def echo(message: types.Message):
    print("Получено сообщение в боте: " + message.text)
    await message.answer(message.text)

async def text(message: types.Message):
    await message.answer('Ты ввел текст: ' + message.text)

async def on_start(message: types.Message):
    await message.answer("Начинаем работать")

async def start():
    logging.basicConfig(
        level=logging.INFO
    )
    logger.error("Error")

    bots = Bot(token)
    dp = Dispatcher()

    dp.startup.register(start_up)
    dp.shutdown.register(sd)

    dp.message.register(on_start, F.text == "/start")
    dp.message.register(text, Text(text = 'Салют'))
    dp.message.register(echo)
    


    await dp.start_polling(bots)

if __name__ == '__main__':
    asyncio.run(start())
