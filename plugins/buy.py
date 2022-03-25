from pymongo.errors import *
from values import *
from pyrogram import (
    Client,
    filters
)
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

@Client.on_message(filters.command(['price','buy' ,'purchase', f'buy@{BOT_USERNAME}' , f'price@{BOT_USERNAME}', f'purchase@{BOT_USERNAME}'],prefixes=['.','/','!'],case_sensitive=False) & filters.text)
async def register(Client,message):
    try: 
        buttons = [[InlineKeyboardButton('🛒 BUY 🛒', callback_data='buy')]]
        reply_markup = InlineKeyboardMarkup(buttons)
        text = """CLICK DOWN"""
        await message.reply_text(text=text,reply_to_message_id=message.message_id,reply_markup=reply_markup)
    except Exception as e:
        print(e)