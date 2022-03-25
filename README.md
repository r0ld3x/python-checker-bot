
## Python Based Checker Bot For Telegram

> Python Based Card Checker Multi Functional Bot For Telegram


## Features

- 10 + Gates
- Code In Python
- etc.

## Demo
<<<<<<< HEAD
![](https://te.legra.ph/file/c885b3318e28ac945a346.mp4)
<!-- <iframe src='https://gfycat.com/ifr/FavoriteThoseCrocodileskink' frameborder='0' scrolling='no' allowfullscreen width='640' height='403'></iframe> -->
=======
![](https://gfycat.com/favoritethosecrocodileskink)
>>>>>>> f30044e (initial commit)





# Deployment

> Download [Python](https://www.python.org/downloads)


### Getting Redis Endpoint And Password

- **Make account on [Redis](redis.com) database**
- **Make subscription with any name and RedisJSON as module**
![get public Endpoint](https://te.legra.ph/file/733d67987bae09c170a48.png)
- **Copy _Public endpoint_**. (looks like `redis-15602.c114.us-east-1-4.ec2.cloud.redislabs.com:15602`)
![get password](https://te.legra.ph/file/c1a8362c9743c68c110b7.png)
- **Copy _Default user password_**. (looks like `1YnkEFFxrK7VrEWKo1AjuDW2LwAsEcWn`)

##### Examples:
``` 
REDIS_URL = 'redis-15602.c114.us-east-1-4.ec2.cloud.redislabs.com'
REDIS_PORT = 15602
REDIS_PASS = '1YnkEFFxrK7VrEWKo1AjuDW2LwAsEcWn'
```
> Replace This Examples With Your Public endpoint and password 

### Getting MongoDB Connection Url

- **Make account on [MongoDB](https://www.mongodb.com/cloud/atlas/register)**
- **Then make a free database with any name**.
- **Add `0.0.0.0` as a ip and your username and password**
![Browse Collections](https://te.legra.ph/file/898ca4a355b6f4e5f4d66.png)
- **Click On `Browse Collections`**.
![Create Database](https://te.legra.ph/file/6be8efeedce051ba84707.png)
- **Click On `Create Database`**.
![](https://telegra.ph/file/89034dba57c6e25c63cb4.png)
- **Paste _Database name_ to `bot` and _Collection name_ to `main`**.
- Click on Create
- Then come back to main screen
![](https://te.legra.ph/file/b7cf1ac188cfb13ca1145.png)
- **Click on `Connect` then Click on `Choose a connection method`**
![](https://te.legra.ph/file/e3ceec1f53ed17495523c.png)
- **Copy your `connection string`.** (looks like `mongodb+srv://root:<password>@cluster0.jwf5a.mongodb.net/myFirstDatabase?retryWrites=true&w=majority`)

##### Examples:
``` 
# Replace <password> with the password for the root user. Replace myFirstDatabase with the name of the database that connections will use by default. Ensure any option params are [URL encoded](https://dochub.mongodb.org/core/atlas-url-encoding).
MONGO_URI = 'mongodb+srv://root:R0ld3x0p@cluster0.jwf5a.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
#Dont Use This URI.
```

# Requirements
- **PC, LAPTIOP, etc**.
- **PYTHON** installed in locally
- **MONGO_URI, REDIS_URL, REDIS_PORT and REDIS_PASS**
- **BRAIN**

  0. Get Bot token from [Botfather](https://t.me/botfather) (The token looks something like `123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11`).
  1. [Login to your Telegram account](https://my.telegram.org/) with the phone number of the developer account to use.
  2. Click under API Development tools.
  3. A Create new application window will appear. Fill in your application details. There is no need to enter any URL, and only the first two fields (App title and Short name) can currently be changed later.
  4. Click on Create application at the end. Remember that your API hash is secret and Telegram won’t let you revoke it. Don’t post it anywhere!
#### Note
```
This API ID and hash is the one used by your application, not your phone number. You can use this API ID and hash with any phone number or even for bot accounts.
```

> Get API_ID AND API_HASH from [my.telegram.org](https://my.telegram.org/)


# Deployment

> Make Sure You have: MONGO_URI, REDIS_URI, REDIS_PASS, REDIS_PORT, API_ID, API_HASH, BOT_TOKEN.

## Connecting Database to bot
- Open `values.py`
- Edit as follows.
![](https://te.legra.ph/file/e46ed7778f5f052e62bad.jpg)

## Adding API_ID , API_HASH, BOT_TOKEN
- Open `main.py`
- Edit as follows.
![](https://te.legra.ph/file/3c8f83d31a7c234897100.jpg)

### Starting Bot
```
pip install -r requirements.txt
python3 -m main.py
```

## Authors

- [@r0ld3x](https://www.github.com/r0ld3x)

## Support:
<<<<<<< HEAD
- All Methods: [Here](https://euphemistic-neglect.000webhostapp.com/)
=======
    All Methods: [Here](https://euphemistic-neglect.000webhostapp.com/)
>>>>>>> f30044e (initial commit)


## License

[MIT](https://choosealicense.com/licenses/mit/)

