import time
from pyrogram import Client
import requests
from requests.exceptions import ProxyError
import re
# import bs4
from values import *
from pyrogram import Client, filters
import json




@Client.on_message(filters.command(["gen", "make"], prefixes=[".", "/", "!"], case_sensitive=False) & filters.text)
async def gen(Client , message):
    try:
        banned_bins = open('files/bannedbin.txt', 'r').readlines()
        verified_gps = open('files/groups.txt', 'r').readlines()
        if (str(message.chat.id) + "\n" not in verified_gps and message.chat.type != "private"):
            await message.reply_text(text= group_not_allowed,reply_to_message_id=message.message_id)
        else:
            if message.reply_to_message is not None:
                message.text = message.reply_to_message.text
            text = f"""<b>WAIT FOR RESULTS</b>"""
            msg = await message.reply_text(text=text,reply_to_message_id=message.message_id)
            await Client.send_chat_action(message.chat.id, "typing")
            find = maindb.find_one({"_id": message.from_user.id})
            if isinstance(find, type(None)) == True:
                await msg.edit_text(use_not_registered)
            elif find['status'] == "F" and message.chat.type == 'private':
                await msg.edit_text(buy_premium)
            else:
                input = re.findall(r"[0-9]+", message.text)
                if len(input) == 0:
                    await msg.edit_text("Your Bin Is Empty")
                if len(input) == 1:
                    cc = input[0]
                    mes = 'x'
                    ano = 'x'
                    cvv = 'x'
                elif len(input[0]) < 6 or len(input[0]) > 16:
                    await msg.edit_text("Your Bin Is Incorrect")
                if len(input) == 2:
                    cc = input[0]
                    mes = input[1]
                    ano = 'x'
                    cvv = 'x'
                if len(input) == 3:
                    cc = input[0]
                    mes = input[1]
                    ano = input[2]
                    cvv = 'x'
                if len(input) == 4:
                    cc = input[0]
                    mes = input[1]
                    ano = input[2]
                    cvv = input[3]
                else:
                    if len(cc) > 15:
                        await msg.edit_text("Your Bin Is Invalid.")
                    else:
                        # lista = cc + "|" + mes + "|" + ano + "|" + cvv
                        bin = cc[:6]
                        res = requests.get("https://jocastabins.herokuapp.com/api/" + bin)
                        if res.status_code != requests.codes.ok or json.loads(res.text)['result'] == False:
                            await msg.edit_text("Your Bin Is Invalid.")
                        elif str(bin) + "\n"in banned_bins or "PREPAID" in res.text:
                            await msg.edit_text("Your Bin Is Banned.")
                        else:
                            bin_data = json.loads(res.text)
                            cc_gen(cc,mes,ano,cvv)
                            cards = ''.join(ccs)
                            ccs.clear()
                            text = f"""
<b>〄</b> CC GENRATOR
<b>○</b> YOUR DATA = {cc}|{mes}|{ano}|{cvv}.
<b>○</b> BANK INFO: <b>{bin_data['data']['bank']} - {bin_data['data']['countryInfo']['code']}({bin_data['data']['countryInfo']['emoji']})</b>
<b>○</b> BIN INFO: <code>{bin}</code> - <b>{bin_data['data']['level']}</b> - <b>{bin_data['data']['type']}</b>

<code>{cards} </code>"""       
                            buttons = [[InlineKeyboardButton('GEN AGAIN', callback_data='gen')]]   
                            reply_markup = InlineKeyboardMarkup(buttons)
                            await msg.edit_text(text,reply_markup=reply_markup)
    except Exception as e:
        print(e)