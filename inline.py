import imp
from aiogram import bot, types, Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import os
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)



urlkb = InlineKeyboardMarkup(run_wigth=2)
urlButton = InlineKeyboardButton(text='Tik-Tok', url='https://vt.tiktok.com/ZSdqaYc2K')
urlButton2 = InlineKeyboardButton(text='Instagram', url='https://www.instagram.com/yondu.pro')

urlkb.add(urlButton, urlButton2)







executor.start_polling(dp, skip_updates=True)