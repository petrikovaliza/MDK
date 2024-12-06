import asyncio
import logging
import random
from config import TOKEN
from aiogram import Bot, Dispatcher, types
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import LinkPreviewOptions
from aiogram.types import FSInputFile, URLInputFile, BufferedInputFile
from contextlib import suppress
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import CommandObject
from aiogram.filters.command import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.enums.dice_emoji import DiceEmoji
from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from datetime import datetime
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
# from aiogram.client.session.aiohttp import AiohttpSession
# import aiohttp
# import ssl

logging.basicConfig(level=logging.INFO)
# session = AiohttpSession()
# session._connector_init = {'ssl': False}
bot = Bot(token=TOKEN)
# , default=DefaultBotProperties(parse_mode=ParseMode.HTML), session=session)
dp = Dispatcher()

# START MENU

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    builder = ReplyKeyboardBuilder()
    builder.row(
        types.KeyboardButton(text="/рандом"),
        types.KeyboardButton(text="/числа")
    )
    builder.row(        
        types.KeyboardButton(text="/ссылка"),
        types.KeyboardButton(text="/гифка")
    )
    builder.row( 
        types.KeyboardButton(text="/эмоджи"),
        types.KeyboardButton(text="/анекдот")
    )
    builder.row(
        types.KeyboardButton(text="/викторина"),
        types.KeyboardButton(text="/животное")
    )
    await message.answer("Что будем делать?", reply_markup=builder.as_markup(resize_keyboard=True))

# ВИКТОРИНА 1

@dp.message(Command("викторина"))
async def cmd_quiz1(message: Message):
    kb = [
        [
            types.KeyboardButton(text="Стокгольм"),
            types.KeyboardButton(text="Осло"),
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    await message.answer("1 вопрос -Столица Швеции?", reply_markup=keyboard)
    
@dp.message(F.text.lower() == "осло")
async def sweden_verno(message: types.Message):
    await message.reply("Неверно:(")
    
@dp.message(F.text.lower() == "стокгольм")
async def sweden_neverno(message: types.Message):
    await message.reply("Абсолютно верно!")

# ВИКТОРИНА 2

    kb = [
        [
            types.KeyboardButton(text="The Beatles"),
            types.KeyboardButton(text="Queen"),
            types.KeyboardButton(text="Led Zeppelin"),
            types.KeyboardButton(text="Pink Floyd"),
            
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    await message.answer("2 - Какая группа исполнила песню «Bohemian Rhapsody»?", reply_markup=keyboard)
    
@dp.message(F.text.lower() == "the beatles")
async def beatles(message: types.Message):
    await message.reply("Неверно:(")
    
@dp.message(F.text.lower() == "pink floyd")
async def pink(message: types.Message):
    await message.reply("Неверно:(")
    
@dp.message(F.text.lower() == "led zeppelin")
async def zeppelin(message: types.Message):
    await message.reply("Неверно:(")

@dp.message(F.text.lower() == "queen")
async def queen(message: types.Message):
    await message.reply("Абсолютно верно!")

# ВИКТОРИНА 3

    kb = [
        [
            types.KeyboardButton(text="100"),
            types.KeyboardButton(text="10"),
            types.KeyboardButton(text="0"),
            types.KeyboardButton(text="1"),
            
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    await message.answer("4 - Как называется число, которое делится без остатка на любое другое число?", reply_markup=keyboard)
    
@dp.message(F.text.lower() == "100")
async def numb100(message: types.Message):
    await message.reply("Неверно:(")
    
@dp.message(F.text.lower() == "10")
async def numb10(message: types.Message):
    await message.reply("Неверно:(")
    
@dp.message(F.text.lower() == "0")
async def numb0(message: types.Message):
    await message.reply("Неверно:(")

@dp.message(F.text.lower() == "1")
async def numb1(message: types.Message):
    await message.reply("Абсолютно верно!")

# ВИКТОРИНА 4

    kb = [
        [
            types.KeyboardButton(text="3"),
            types.KeyboardButton(text="1"),
            types.KeyboardButton(text="4"),
            types.KeyboardButton(text="2"),
            
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    await message.answer("4 - Сколько сердец у осьминога?", reply_markup=keyboard)
    
@dp.message(F.text.lower() == "4")
async def heart_4(message: types.Message):
    await message.reply("Неверно:(")
    
@dp.message(F.text.lower() == "2")
async def heart_2(message: types.Message):
    await message.reply("Неверно:(")
    
@dp.message(F.text.lower() == "1")
async def heart_1(message: types.Message):
    await message.reply("Неверно:(")

@dp.message(F.text.lower() == "3")
async def heart_3(message: types.Message):
    await message.reply("Абсолютно верно!")

# ВИКТОРИНА 5

    kb = [
        [KeyboardButton(text="Для терморегуляции")],
        [KeyboardButton(text="Чтобы сбивать с толку хищников")],
        [KeyboardButton(text="Для маскировки")],
        [KeyboardButton(text="Это просто рисунок, не имеющий особого значения")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    await message.answer("5 - Почему зебры полосатые?", reply_markup=keyboard)
    
@dp.message(F.text.lower() == "для терморегуляции")
async def zebra1(message: types.Message):
    await message.reply("Неверно:(")
    
@dp.message(F.text.lower() == "это просто рисунок, не имеющий особого значения")
async def zebra2(message: types.Message):
    await message.reply("Неверно:(")
    
@dp.message(F.text.lower() == "для маскировки")
async def zebra3(message: types.Message):
    await message.reply("Неверно:(")

@dp.message(F.text.lower() == "чтобы сбивать с толку хищников")
async def zebra4(message: types.Message):
    await message.reply("Абсолютно верно!")

# ВИКТОРИНА 6

    kb = [
        [
            types.KeyboardButton(text="Лев"),
            types.KeyboardButton(text="Газель Томсона "),
            types.KeyboardButton(text="Гепард"),
            types.KeyboardButton(text="Антилопа гну"),
            
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    await message.answer("6 - Какое животное считается самым быстрым на суше?", reply_markup=keyboard)
    
@dp.message(F.text.lower() == "лев")
async def lev(message: types.Message):
    await message.reply("Неверно:(")
    
@dp.message(F.text.lower() == "газель томсона")
async def gazel(message: types.Message):
    await message.reply("Неверно:(")
    
@dp.message(F.text.lower() == "антилопа гну")
async def antilopa(message: types.Message):
    await message.reply("Неверно:(")

@dp.message(F.text.lower() == "гепард")
async def gepard(message: types.Message):
    await message.reply("Абсолютно верно!")


# ВИКТОРИНА 7
    
    kb = [
        [
            types.KeyboardButton(text="Сова"),
            types.KeyboardButton(text="Колибри"),
            types.KeyboardButton(text="Летучая мышь"),
            types.KeyboardButton(text="Кот"),
            
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    await message.answer("7 - Какой хищник имеет самые большие глаза относительно своего размера тела?", reply_markup=keyboard)
    
@dp.message(F.text.lower() == "кот")
async def cat(message: types.Message):
    await message.reply("Неверно:(")
    
@dp.message(F.text.lower() == "колибри")
async def colibri(message: types.Message):
    await message.reply("Неверно:(")
    
@dp.message(F.text.lower() == "летучая мышь")
async def letmush(message: types.Message):
    await message.reply("Неверно:(")

@dp.message(F.text.lower() == "сова")
async def sova(message: types.Message):
    await message.reply("Абсолютно верно!")


# ВИКТОРИНА 8

    kb = [
            [KeyboardButton(text="Летающие лемуры")],
            [KeyboardButton(text="Белки-летяги")],
            [KeyboardButton(text="Сумчатые летуны")],
            [KeyboardButton(text="Летучие мыши")],
        ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    await message.answer("8 - Кто является единственным млекопитающим, который может летать?", reply_markup=keyboard)
    
@dp.message(F.text.lower() == "летающие лемуры")
async def lemur(message: types.Message):
    await message.reply("Неверно:(")
    
@dp.message(F.text.lower() == "белки-летяги")
async def belki(message: types.Message):
    await message.reply("Неверно:(")
    
@dp.message(F.text.lower() == "сумчатые летуны")
async def sumletun(message: types.Message):
    await message.reply("Неверно:(")

@dp.message(F.text.lower() == "летучие мыши")
async def let_mush(message: types.Message):
    await message.reply("Абсолютно верно!")

# ЛЮБИМОЕ ЖИВОТНОЕ

@dp.message(Command("животное"))
async def cmd_animal(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="Кошка"),
            types.KeyboardButton(text="Собака"),
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    await message.answer("Выберите животное", reply_markup=keyboard)

@dp.message(F.text.lower() == "кошка")
async def cat(message: types.Message):
    await message.reply("Они мои самые любимые животные тоже!", reply_markup=types.ReplyKeyboardRemove())
    
@dp.message(F.text.lower() == "собака")
async def dog(message: types.Message):
    await message.reply("Они очень милые!", reply_markup=types.ReplyKeyboardRemove())

# ССЫЛКА

@dp.message(Command("ссылка"))
async def cmd_links(message: Message):
    links_text = (
        "https://www.youtube.com/channel/UCdKuE7a2QZeHPhDntXVZ91w?ysclid=m2wuvvdq5l368349427"
    )
    options_3 = LinkPreviewOptions(
        url="https://www.youtube.com/channel/UCdKuE7a2QZeHPhDntXVZ91w?ysclid=m2wuvvdq5l368349427",
        prefer_large_media=True
    )
    await message.answer(
        f"Куплик\n{links_text}",
        link_preview_options=options_3
    )

# ГИФКА

my_gif = FSInputFile("cat.gif")
@dp.message(Command("гифка"))
async def send_gif(message: Message):
    await message.answer_animation(my_gif, caption='Я и программирование:', show_caption_above_media=True)
    await asyncio.sleep(2)

# ЭМОДЖИ

@dp.message(Command("эмоджи"))
async def cmd_dice(message: types.Message):
    await message.answer_dice(emoji=DiceEmoji.BOWLING)

# РАНДОМ

@dp.message(Command("рандом"))
async def cmd_random(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Нажми меня",
        callback_data="random_value")
    )
    await message.answer(
        "Нажмите на кнопку, чтобы бот отправил число от 1 до 10",
        reply_markup=builder.as_markup()
    )

@dp.callback_query(F.data == "random_value")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer(str(random.randint(1, 10)))
    await callback.answer(
        text="Спасибо, что воспользовались ботом!",
        show_alert=True
    )

# ЧИСЛА +1 -1

user_data = {}

def get_keyboard():
    buttons = [
        [
            types.InlineKeyboardButton(text="-1", callback_data="num_decr"),
            types.InlineKeyboardButton(text="+1", callback_data="num_incr")
        ],
        [types.InlineKeyboardButton(text="Подтвердить", callback_data="num_finish")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


async def update_num_text(message: types.Message, new_value: int):
    with suppress(TelegramBadRequest):
        await message.edit_text(
            f"Укажите число: {new_value}",
            reply_markup=get_keyboard()
        )

@dp.message(Command("числа"))
async def cmd_numbers(message: types.Message):
    user_data[message.from_user.id] = 0
    await message.answer("Укажите число: 0", reply_markup=get_keyboard())

@dp.callback_query(F.data.startswith("num_"))
async def callbacks_num(callback: types.CallbackQuery):
    user_value = user_data.get(callback.from_user.id, 0)
    action = callback.data.split("_")[1]

    if action == "incr":
        user_data[callback.from_user.id] = user_value+1
        await update_num_text(callback.message, user_value+1)
    elif action == "decr":
        user_data[callback.from_user.id] = user_value-1
        await update_num_text(callback.message, user_value-1)
    elif action == "finish":
        await callback.message.edit_text(f"Итого: {user_value}")

    await callback.answer()

# АНЕКДОТ

@dp.message(Command("анекдот"))
async def jokes(message: types.Message):
    await message.reply("\nДочь ты пила? \nНет мама, я топор!")
    
async def main():
    # sslcontext = ssl.create_default_context()
    # sslcontext.check_hostname = False
    # sslcontext.verify_mode = ssl.CERT_NONE
    # async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=sslcontext)) as session:
        await dp.start_polling(bot)
    
if __name__ == "__main__":
    asyncio.run(main())

    