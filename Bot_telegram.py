from curses import curs_set
from aiogram.utils import executor
from create_bot import dp, bot
from data_base import sqlite_db
from aiogram import Bot, Dispatcher
import config, os


bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)


async def on_startup(_):
    print('Bot online')
    sqlite_db.sql_start()

async def on_startup(dp):
    await bot.set_webhook(config.URL_APP)

async def on_shutdowh(dp):
    await bot.delete_webhook()
 

from handlers import client, admin, other

client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
other.register_handlers_other(dp)


executor.start_webhook(
    dispatcher= dp,
    webhook_path= '',
    on_startup=on_startup,
    on_shutdown=on_shutdowh,
    skip_updates=True,
    host="0.0.0.0",
    port=int(os.environ.get("PORT", 5000)))
