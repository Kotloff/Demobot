
from aiogram import Dispatcher, types
from create_bot import bot
from keyboard import kb_client
from data_base import sqlite_db
from keyboard.client_kb import urlkb

async def commands_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Greetings stranger', reply_markup=kb_client)
    except:
        await message.reply('Talk to me via PM:\nhttps://t.me/yondu7bot')

async def commands_abil(message : types.Message):
    await bot.send_message(message.from_user.id, 'I can show you\nWhat my Master did\nHe made me by his own')   


async def commands_req(message : types.Message):
    await bot.send_message(message.from_user.id, 'I want to serv my Master')


async def about_command(message : types.Message):
    await sqlite_db.sql_read(message)

# @dp.message_handler(commands='Links')
async def url_command(message : types.Message):
    await message.answer('Links:', reply_markup=urlkb)

def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(commands_start, commands=['Start', 'Help'])    
    dp.register_message_handler(commands_abil, commands=['Abilities'])
    dp.register_message_handler(commands_req, commands=['Demands'])
    dp.register_message_handler(url_command, commands=['Links'])