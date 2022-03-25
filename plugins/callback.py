import os
import pyrogram
from pyrogram.types.bots_and_keyboards import inline_keyboard_button
from values import *
from pyrogram import filters, Client
from pyrogram import client
from pyrogram.methods import messages
import pyrogram.errors
from pyrogram.errors import RPCError
from pyrogram.errors import BadRequest, Forbidden
from pyrogram.types import (
    InlineQueryResultArticle, InputTextMessageContent,
    InlineKeyboardMarkup, InlineKeyboardButton,
    CallbackQuery, InlineQuery, update)


async def myacc(Client, message , update):
  buttons = [
    [
        InlineKeyboardButton('💳 MY LIVE 💳', callback_data='mylives'),
        InlineKeyboardButton('🚪 GATES 🚪', callback_data='gates')
    ],
    [
        InlineKeyboardButton('🚪 CLOSE 🚪', callback_data='close')
    ]
    ]
  reply_markup = InlineKeyboardMarkup(buttons)
  find = maindb.find_one({
    "_id": message.reply_to_message.from_user.id,
})
  if isinstance(find, type(None)) == True:
    text = """ Register First Hit /takeme to register yourself"""
    await Client.answer_callback_query(
            callback_query_id=update.id,
            text=text,
            show_alert="true"
          )
  else:
    antispam_time = int(antidb.get(message.reply_to_message.from_user.id).decode("utf-8"))
    text = f"""
<b>〄</b> User Information:-
<b>○</b> First Name: <b>{message.reply_to_message.from_user.first_name}</b>
<b>○</b> User Name: <b>{message.reply_to_message.from_user.username}</b>
<b>○</b> User Id: <b><code>{message.reply_to_message.from_user.id}</code></b>
<b>○</b> Limited: <b>{message.reply_to_message.from_user.is_restricted}</b>
<b>○</b> Profile Link: <b><a href="tg://user?id={message.reply_to_message.from_user.id}">Click Here</a></b>
<b>○</b> Profile Image: <b><a href="{find['image']}">Click Here</a></b>

<b>〄</b> User Database Information:-
<b>○</b> Role: <b>{find['role']}</b>
<b>○</b> Plan: <b>{find['plan']}</b>
<b>○</b> Status: <b>{find['status']}</b>
<b>○</b> Credits: <b>{find['credits']}</b>
<b>○</b> Live Cards: <b>COMING SOON</b>
<b>○</b> AntiSpam Time: <b>{datetime.utcfromtimestamp(antispam_time).strftime('%H:%M:%S %d-%m-%Y')}</b>

<b>〄</b> Chat Information:-
<b>○</b> Chat Name: <b>{message.reply_to_message.chat.title}</b>
<b>○</b> User Name: <b>{message.reply_to_message.chat.username}</b>
<b>○</b> Chat Id: <b><code>{message.reply_to_message.chat.id}</code></b>
<b>○</b> Chat Type: <b>{message.reply_to_message.chat.type.capitalize()}</b>
      """
    await Client.edit_message_text(
        chat_id=message.chat.id,
        text=text,
        reply_markup=reply_markup,
        message_id=message.message_id,
        disable_web_page_preview=True
    )
    
    
async def gates(Client, message,update):
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
  await Client.edit_message_text(
      chat_id=message.chat.id,
      text=text,
      reply_markup=reply_markup,
      message_id=message.message_id,
      disable_web_page_preview=True
  )
  
  
async def paid(Client, message,update):
  buttons = [
  [
      InlineKeyboardButton('🟢 AUTH 🟢', callback_data='auth'), 
      InlineKeyboardButton('🔴 CHARGE 🔴', callback_data='charge')
  ],
  [
      InlineKeyboardButton('🟣 EXTRA 🟣', callback_data='extra'),
      InlineKeyboardButton('🛠️ TOOLS 🛠️', callback_data='tools')
  ],
  [
      InlineKeyboardButton('🚪 CLOSE 🚪', callback_data='close')
  ]
  ]
  reply_markup = InlineKeyboardMarkup(buttons)
  text="""Check Down My Paid Commands"""
  await Client.edit_message_text(
      chat_id=message.chat.id,
      text=text,
      reply_markup=reply_markup,
      message_id=message.message_id,
      disable_web_page_preview=True
  )
    
    
    
    
async def free(Client, message , update):
  buttons = [
    [
        InlineKeyboardButton('↩️ RETURN ↩️', callback_data='gates')
    ],
    [
        InlineKeyboardButton('🚪 CLOSE 🚪', callback_data='close')
    ]
    ]
  reply_markup = InlineKeyboardMarkup(buttons)
  text = """
<b>〄</b> Free Gates:-

<b>○</b> <b>/ca</b>: <b>Stripe Auth [1]</b> || <b>Status: On ✅</b>
<b>○</b> <b>/ch</b>: <b>Stripe Auth [2]</b> || <b>Status: On ✅</b>
<b>○</b> <b>/ci</b>: <b>Stripe Auth [3]</b> || <b>Status: On ✅</b>
"""
  await Client.edit_message_text(
      chat_id=message.chat.id,
      text=text,
      reply_markup=reply_markup,
      message_id=message.message_id,
      disable_web_page_preview=True
  )
  
async def auth(Client, message , update):
  buttons = [
    [
        InlineKeyboardButton('🛒 BUY 🛒', callback_data='buy'),
        InlineKeyboardButton('🔴 CHARGE 🔴', callback_data='charge')
    ],
    [
        InlineKeyboardButton('↩️ RETURN ↩️', callback_data='gates'),
        InlineKeyboardButton('🚪 CLOSE 🚪', callback_data='close')
    ]
    ]
  reply_markup = InlineKeyboardMarkup(buttons)
# abcdefghijklmnopqrstuvwxyz
  text = """
<b>〄</b> Auth Gates:-
<b>📢</b> <b><i>2 credits per check.</i></b>
<b>○</b> <b>/sa</b>: <b>Stripe [1]</b> || <b>Status: On ✅</b>
<b>○</b> <b>/sc</b>: <b>Stripe [2]</b> || <b>Status: On ✅</b>
<b>○</b> <b>/sf</b>: <b>Stripe [3]</b> || <b>Status: On ✅</b>
<b>○</b> <b>/sh</b>: <b>Stripe [4]</b> || <b>Status: On ✅</b>
<b>○</b> <b>/si</b>: <b>Stripe [5]</b> || <b>Status: On ✅</b>
<b>○</b> <b>/sl</b>: <b>Stripe [6]</b> || <b>Status: On ✅</b>
<b>○</b> <b>/sm</b>: <b>Stripe [7]</b> || <b>Status: On ✅</b>
<b>○</b> <b>/so</b>: <b>Stripe [8]</b> || <b>Status: On ✅</b>
<b>○</b> <b>/sp</b>: <b>Stripe [9]</b> || <b>Status: On ✅</b>
<b>○</b> <b>/ss</b>: <b>Stripe [10]</b> || <b>Status: On ✅</b>
<b>○</b> <b>/st</b>: <b>Stripe [11]</b> || <b>Status: On ✅</b>
<b>○</b> <b>/su</b>: <b>Stripe [12]</b> || <b>Status: On ✅</b>
"""
  await Client.edit_message_text(
      chat_id=message.chat.id,
      text=text,
      reply_markup=reply_markup,
      message_id=message.message_id,
      disable_web_page_preview=True
  )
  

async def charge(Client, message , update):
  buttons = [
    [
        InlineKeyboardButton('🛒 BUY 🛒', callback_data='buy'),
        InlineKeyboardButton('🟣 EXTRA 🟣', callback_data='extra')
    ],
    [
        InlineKeyboardButton('↩️ RETURN ↩️', callback_data='gates'),
        InlineKeyboardButton('🚪 CLOSE 🚪', callback_data='close')
    ]
    ]
  reply_markup = InlineKeyboardMarkup(buttons)
  text = """
<b>〄</b> Charge Gates:-
<b>📢</b> <b><i>2 credits per check.</i></b>

<b>○</b> <b>/za</b>: <b>Stripe [1]</b> || <b>Status: On ✅ </b>
<b>○</b> <b>/zc</b>: <b>Stripe [2]</b> || <b>Status: On ✅ </b>
<b>○</b> <b>/zm</b>: <b>Stripe [4]</b> || <b>Status: On ✅ </b>
<b>○</b> <b>/zo</b>: <b>Stripe [5]</b> || <b>Status: On ✅ </b>
<b>○</b> <b>/zt</b>: <b>Stripe [6]</b> || <b>Status: Off ❌</b>
<b>○</b> <b>/zu</b>: <b>Stripe [7]</b> || <b>Status: Off ❌</b>
"""
  await Client.edit_message_text(
      chat_id=message.chat.id,
      text=text,
      reply_markup=reply_markup,
      message_id=message.message_id,
      disable_web_page_preview=True
  )

async def extra(Client, message , update):
  buttons = [
    [
        InlineKeyboardButton('🛒 BUY 🛒', callback_data='buy'),
        InlineKeyboardButton('🟢 AUTH 🟢', callback_data='auth')
    ],
    [
        InlineKeyboardButton('↩️ RETURN ↩️', callback_data='paid'),
        InlineKeyboardButton('🚪 CLOSE 🚪', callback_data='close')
    ]
    ]
  reply_markup = InlineKeyboardMarkup(buttons)
  text = """
<b>〄</b> Extra Gates:-

<b>○</b> <b>/za</b>: <b>Stripe Auth [1]</b> || <b>Status: Off ❌</b>
<b>○</b> <b>/zc</b>: <b>Stripe Auth [2]</b> || <b>Status: Off ❌</b>
<b>○</b> <b>/zm</b>: <b>Stripe Auth [4]</b> || <b>Status: Off ❌</b>
<b>○</b> <b>/zo</b>: <b>Stripe Auth [5]</b> || <b>Status: Off ❌</b>
<b>○</b> <b>/zt</b>: <b>Stripe Auth [6]</b> || <b>Status: Off ❌</b>
<b>○</b> <b>/zu</b>: <b>Stripe Auth [7]</b> || <b>Status: Off ❌</b>
"""
  await Client.edit_message_text(
      chat_id=message.chat.id,
      text=text,
      reply_markup=reply_markup,
      message_id=message.message_id,
      disable_web_page_preview=True
  )
  
  
async def buy(Client, message , update):
  buttons = [
    [
        InlineKeyboardButton('🛒 BUY 🛒', url='https://t.me/r0ld3x'),
        InlineKeyboardButton('ℹ CHANNEL ℹ', url='https://t.me/roldexverse')
    ],
    [
        InlineKeyboardButton('↩️ RETURN ↩️', callback_data='gates'),
        InlineKeyboardButton('🚪 CLOSE 🚪', callback_data='close')
    ]
    ]
  reply_markup = InlineKeyboardMarkup(buttons)
  text = """
<b>〄</b> Prices:-

<b>○</b> <b>5$</b>: <b>250 Credits</b> || <b>Access all gates</b>
<b>○</b> <b>10$</b>: <b>600 Credits</b> || <b>Access all gates</b>
<b>○</b> <b>20$</b>: <b>1500 Credits</b> || <b>Access all gates</b>
<b>○</b> <b>25$</b>: <b>3000 Credits</b> || <b>Access all gates</b>
<b>📢</b> <b><i>ONLY ACCEPTED CRYPTO CURRRENCY && UPI.</i></b>
"""
  await Client.edit_message_text(
      chat_id=message.chat.id,
      text=text,
      reply_markup=reply_markup,
      message_id=message.message_id,
      disable_web_page_preview=True
  )

async def gen(Client, message , update):
  buttons = [
    [
        InlineKeyboardButton('🛒 BUY 🛒', url='https://t.me/r0ld3x'),
        InlineKeyboardButton('ℹ CHANNEL ℹ', url='https://t.me/roldexverse')
    ],
    [
        InlineKeyboardButton('↩️ RETURN ↩️', callback_data='gates'),
        InlineKeyboardButton('🚪 CLOSE 🚪', callback_data='close')
    ]
    ]
  reply_markup = InlineKeyboardMarkup(buttons)
  msg = re.search(r'YOUR DATA = (.*).\n', update.message.text).group(1)
  input = re.findall(r"[0-9]+", msg)
  if len(input) == 0:
      text = "Your Bin Is Empty"
      await Client.edit_message_text(chat_id=message.chat.id,text=text,reply_markup=reply_markup,message_id=message.message_id)
  if len(input) == 1:
      cc = input[0]
      mes = 'x'
      ano = 'x'
      cvv = 'x'
  elif len(input[0]) < 6 or len(input[0]) > 16:
      text = "Your Bin Is Incorrect"
      await Client.edit_message_text(chat_id=message.chat.id,text=text,reply_markup=reply_markup,message_id=message.message_id)
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
          await Client.edit_message_text(chat_id=message.chat.id,text=text,reply_markup=reply_markup,message_id=message.message_id)
      else:
        bin = cc[:6]
        res = requests.get("https://adyen-enc-and-bin-info.herokuapp.com/bin/" + bin)
        if res.status_code != requests.codes.ok or json.loads(res.text)['result'] == False:
            text = "Your Bin Is Invalid."
            await Client.edit_message_text(chat_id=message.chat.id,text=text,reply_markup=reply_markup,message_id=message.message_id)
        elif str(bin) + "\n"in banned_bins or "PREPAID" in res.text:
            text = "Your Bin Is Banned."
            await Client.edit_message_text(chat_id=message.chat.id,text=text,reply_markup=reply_markup,message_id=message.message_id)
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
            await Client.edit_message_text(
                chat_id=message.chat.id,
                text=text,
                reply_markup=reply_markup,
                message_id=message.message_id,
                disable_web_page_preview=True
  )
  

async def tools(Client, message , update):
  buttons = [
    [
        InlineKeyboardButton('↩️ RETURN ↩️', callback_data='gates')
    ],
    [
        InlineKeyboardButton('🚪 CLOSE 🚪', callback_data='close')
    ]
    ]
  reply_markup = InlineKeyboardMarkup(buttons)
  text = """
<b>〄</b> Tools:-

<b>○</b> <b>/info</b>: <b>Your Information</b>
<b>○</b> <b>/bin</b>: <b>Bin Information</b>
<b>○</b> <b>/gen</b>: <b>Genrate ccs from bin</b>
<b>○</b> <b>/vbv</b>: <b>Check for vbv</b>
"""
# <b>/ci</b>: <b>Stripe Auth</b> || <b>Status: On ✅</b>
  await Client.edit_message_text(
      chat_id=message.chat.id,
      text=text,
      reply_markup=reply_markup,
      message_id=message.message_id,
      disable_web_page_preview=True
  )




@Client.on_callback_query()
async def button(Client, update):
      cb_data = update.data
      try: 
        text = f"""Action Not Allowed
This Buttons Is only For {update.message.reply_to_message.from_user.first_name} [{update.message.reply_to_message.from_user.id}]"""""
        if update.message.reply_to_message.from_user.id == update.from_user.id:
          if "myacc" in cb_data:
            await myacc(Client, update.message,update)
          elif "close" in cb_data:
            await update.message.delete() 
          elif "gates" in cb_data:
            await gates(Client, update.message,update)
          elif "free" in cb_data:
            await free(Client, update.message,update)
          elif "paid" in cb_data:
                await paid(Client, update.message,update)
          elif "auth" in cb_data:
                await auth(Client, update.message,update)
          elif "charge" in cb_data:
                await charge(Client, update.message,update)
          elif "extra" in cb_data:
                # await extra(Client, update.message,update)
            await Client.answer_callback_query(
            callback_query_id=update.id,
            text="🔜Coming Soon🔜",
            show_alert="true"
          )
          elif "buy" in cb_data:
                await buy(Client, update.message,update)
          elif "gen" in cb_data:
                await gen(Client, update.message,update)
          elif "tools" in cb_data:
              await tools(Client, update.message,update)
          elif "mylives" in cb_data:
            await Client.answer_callback_query(
            callback_query_id=update.id,
            text="🔜Coming Soon🔜",
            show_alert="true"
          )
        else:
            await Client.answer_callback_query(
            callback_query_id=update.id,
            text=text,
            show_alert="true"
          )
      except RPCError as e:
          print(e)
      except BadRequest as e:
          print(e)
      except Forbidden as e:
          print(e)
        
        
        
# import timeit

# start = timeit.timeit()
# print("hello")
# end = timeit.timeit()
# print(end - start)