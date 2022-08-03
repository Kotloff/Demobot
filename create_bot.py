from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher import dispatcher
import os, config

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)