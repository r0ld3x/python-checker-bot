from datetime import datetime
import time
import pymongo
from telegraph import upload_file
import pymongo.errors
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
# from _startup import *
from pyrogram.errors import RPCError
from pyrogram.errors import BadRequest, Forbidden
        # buttons = InlineKeyboardMarkup([
        # [
        #     InlineKeyboardButton('GATES', callback_data='home1'),
        #     InlineKeyboardButton('TOOLS', callback_data='close')
        # ],
        # [
        #     InlineKeyboardButton('OWNER', url='http://telegram.me/roldexverse'),
        #     InlineKeyboardButton('RETURN', url='https://github.com/r0ld3x/TELEGRAPH-BOT')
        # ]
        # ]
        # )

@Client.on_message(filters.command('info',prefixes=['.','/','!'],case_sensitive=False))
@Client.on_message(filters.command('myacc',prefixes=['.','/','!'],case_sensitive=False))
async def info(Client, message):
    try:
        verified_gps = open('files/groups.txt', 'r').readlines()
        if (str(message.chat.id) + "\n" not in verified_gps and message.chat.type != "private"):
            await message.reply_text(text= group_not_allowed,reply_to_message_id=message.message_id)
        else:
            msg = await message.reply_text(text="<b>Wait For Result</b>",reply_to_message_id=message.message_id)
            await Client.send_chat_action(message.chat.id, "typing")
            find = maindb.find_one({
                "_id": message.from_user.id,
            })
            if isinstance(find, type(None)) == True:
                text = """<b>Register First Hit /takeme to register me</b>"""
                await msg.edit_text(text)
            else:
                if  isinstance(int(antidb.get(message.from_user.id)), type(None)) == True:
                    text = """<b>Register First Hit /takeme </b>"""
                    await msg.edit_text(text)
                else:
                    antispam_time = int(antidb.get(message.from_user.id).decode("utf-8"))
                    text = f"""
<b>〄</b> User Information:-
<b>○</b> First Name: <b>{message.from_user.first_name}</b>
<b>○</b> User Name: <b>{message.from_user.username}</b>
<b>○</b> User Id: <b><code>{message.from_user.id}</code></b>
<b>○</b> Limited: <b>{message.from_user.is_restricted}</b>
<b>○</b> Profile Link: <b><a href="tg://user?id={message.from_user.id}">Click Here</a></b>
<b>○</b> Profile Image: <b><a href="{find['image']}">Click Here</a></b>

<b>〄</b> User Database Information:-
<b>○</b> Role: <b>{find['role']}</b>
<b>○</b> Plan: <b>{find['plan']}</b>
<b>○</b> Status: <b>{find['status']}</b>
<b>○</b> Credits: <b>{find['credits']}</b>
<b>○</b> Live Cards: <b>COMING SOON</b>
<b>○</b> AntiSpam Time: <b>{datetime.utcfromtimestamp(antispam_time).strftime('%H:%M:%S %d-%m-%Y')}</b>

<b>〄</b> Chat Information:-
<b>○</b> Chat Name: <b>{message.chat.title}</b>
<b>○</b> User Name: <b>{message.chat.username}</b>
<b>○</b> Chat Id: <b><code>{message.chat.id}</code></b>
<b>○</b> Chat Type: <b>{message.chat.type.capitalize()}</b>
    """
                    await msg.edit_text(text,disable_web_page_preview=True)
# <b>○</b> Message Type: <b>{message.from_user.type}</b>
        # await Client.send_message(chat_id=message.chat.id,text=text,reply_to_message_id=message.message_id,reply_markup=buttons)
    except Exception as e:
        await Client.send_message(chat_id=loggp,text=e)
        print(e) 
                # if message.from_user.photo is None:
                #     userimage = "https://te.legra.ph/file/8692b409921efe361831f.png"
                # else:
                #     user_image_path = (f"./userimage/{message.from_user.id}.jpg")
                #     await Client.download_media(message=message.from_user.photo.big_file_id, file_name=user_image_path)
                #     tlink = upload_file(user_image_path)
                #     userimage = f"https://telegra.ph{tlink[0]}"
                #     os.remove(user_image_path)
                #     mydict = {
                #         "_id": message.from_user.id,
                #         "id": message.from_user.id,
                #         "username": message.from_user.username,
                #         "plan": "Free Plan",
                #         "role": "Free User",
                #         "status": "F",
                #         "credits": 0,
                #         "exptime": "Never",
                #         "Image": userimage,
                #         "antispam": int(time.time()),
                #     }
                # x = maindb.insert_one(mydict)
                # print(x.inserted_id)
                # find = maindb.getLastInsertedDocument.find();
                # print("getLastInsertedDocument:",find)
                # file = open('users.txt', 'a+') 
                # file.write(str(message.from_user.id))
                # print("user created")
                # file.close()