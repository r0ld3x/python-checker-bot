import math
import time
from typing import Text
import requests
import logging
from pyrogram import Client
from pyrogram.errors import RPCError
from pyrogram.errors import BadRequest, Forbidden
logging.basicConfig(level=logging.INFO)
import time
from pyrogram.errors import FloodWait
from pyrogram.handlers import MessageHandler
import requests	
import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import re
import sys 
import os
from values import *
from pyrogram import (
    Client,
    filters
)
import json
@Client.on_message(filters.command('addbin',prefixes=['.','/','!'],case_sensitive=False) & filters.text)
async def banbin(Client, message):
    try:
        if str(message.from_user.id) + "\n" in admins:
            file = open('files/bannedbin.txt', 'r') 
            input = lista(message.text)
            bin = input[:6]
            if str(bin) + "\n" not in file.readlines():
                file = open('files/bannedbin.txt', 'a+') 
                file.write(str(bin) + "\n")
                file.close()
                await message.reply_text(text="<b>BANNED</b>",reply_to_message_id=message.message_id)
            else:
                await message.reply_text(text="<b>ALREADY BANNED</b>",reply_to_message_id=message.message_id)
    except IndexError as e:
        print(e)
    except Exception as e:
        print(e)  

