from os import curdir
import sqlite3 as sq
from create_bot import dp, bot
import psycopg2
import os

def sql_start():
    global base, cur

async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO about VALUES (?, ?, ?, ?)', tuple(data.values()))
        base.commit()

async def sql_read(message):

    for ret in cur.execute('SELECT * FROM about').fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nDescription: {ret[2]}\nYear: {ret[-1]}')

async def sql_read2():
    return cur.execute('SELECT * FROM about').fetchall()


async def sql_delete_command(data):
    cur.execute('DELETE FROM about WHERE name == ?', (data,))
    base.commit()