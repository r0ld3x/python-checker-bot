# from datetime import datetime
# import asyncio
from bson.json_util import dumps,RELAXED_JSON_OPTIONS
# import json
import time
from telegraph import upload_file
# from pymongo.mongo_client import MongoClient
# import pymongo.errors
from pymongo.errors import *
from values import *
from pyrogram import (
    Client,
    filters
)
# from pyrogram.types import (
#     InlineKeyboardButton,
#     InlineKeyboardMarkup
# )
from datetime import datetime
@Client.on_message(filters.command(['cmds','gates' ,'commands', f'gates@{BOT_USERNAME}' , f'cmds@{BOT_USERNAME}', f'commands@{BOT_USERNAME}'],prefixes=['.','/','!'],case_sensitive=False) & filters.text)
async def cmds(Client,message):
    try:
        buttons = [
        [
            InlineKeyboardButton('🎁 FREE 🎁', callback_data='free'), 
            InlineKeyboardButton('💲 PAID 💲', callback_data='paid')
        ],
        [
            InlineKeyboardButton('🛠️ TOOLS 🛠️', callback_data='tools'),
            InlineKeyboardButton('🚪 CLOSE 🚪', callback_data='close')
        ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        text="""Check Down My Commands"""
        await message.reply_text(text=text,reply_to_message_id=message.message_id,reply_markup=reply_markup)
    except Exception as e:
        print(e)