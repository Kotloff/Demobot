from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from numpy import insert
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


b1 = KeyboardButton('/Abilities')
b2 = KeyboardButton('/Demands')
b3 = KeyboardButton('/Links')

urlkb = InlineKeyboardMarkup(run_wigth=2)
urlButton = InlineKeyboardButton(text='Tik-Tok', url='https://vt.tiktok.com/ZSdqaYc2K')
urlButton2 = InlineKeyboardButton(text='Instagram', url='https://www.instagram.com/yondu.pro')

urlkb.add(urlButton, urlButton2)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(b1).add(b2).add(b3)