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
    filters)

@Client.on_message(filters.command('addgp',prefixes=['.','/','!'],case_sensitive=False) & filters.text)
async def bin(Client, message):
    try:
        if str(message.from_user.id) + "\n" in admins:
            file = open('files/groups.txt', 'r')
            if str(message.chat.id) + "\n" not in file.readlines():
                file = open('files/groups.txt', 'a+') 
                file.write(str(message.chat.id) + "\n")
                file.close()
                await message.reply_text(text="<b>ADDED</b>",reply_to_message_id=message.message_id)
            else:
                await message.reply_text(text="<b>ALREADY ADDED</b>",reply_to_message_id=message.message_id)
    except IndexError as e:
        print(e)
    except Exception as e:
        print(e)  

