import os
import time
import asyncio
import pyrogram
import logging
import time
import hashlib
from urllib.request import urlopen, Request
from pyrogram import idle


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler(
                        'log.txt'), logging.StreamHandler()],
                    level=logging.INFO)

logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.ERROR)

banner = (
    "\033[96m"
    + r"""
  __  __             _____ _             _    
 |  \/  |           / ____| |           | |   
 | \  / |_ __      | (___ | |_ __ _ _ __| | __
 | |\/| | '__|      \___ \| __/ _` | '__| |/ /
 | |  | | |     _   ____) | || (_| | |  |   < 
 |_|  |_|_|    (_) |_____/ \__\__,_|_|  |_|\_\

"""
)

#logging.info("Starting Assistant...")
#logging.info(banner)
#logging.info("𝑨𝒔𝒔𝒊𝒔𝒕𝒂𝒏𝒕 𝒉𝒂𝒔 𝒃𝒆𝒆𝒏 𝒔𝒕𝒂𝒓𝒕𝒆𝒅 𝒔𝒖𝒄𝒄𝒆𝒔𝒔𝒇𝒖𝒍𝒍𝒚")
app = pyrogram.Client(
        "Notify me",
        bot_token="5539979950:AAFNPzxDIBUdtdGjBCRzUbbgd0O5JkDL5cU",
        api_id=1612723,
        api_hash="eb3bc0998f7a134318a6d5763e9d0d49",
    )
app.start()
logging.info("Starting Assistant...")
logging.info(banner)
logging.info("𝑨𝒔𝒔𝒊𝒔𝒕𝒂𝒏𝒕 𝒉𝒂𝒔 𝒃𝒆𝒆𝒏 𝒔𝒕𝒂𝒓𝒕𝒆𝒅 𝒔𝒖𝒄𝒄𝒆𝒔𝒔𝒇𝒖𝒍𝒍𝒚")

app.send_message(-1001330957197,"started")
url = Request('https://satyendra.tech/',
              headers={'User-Agent': 'Mozilla/5.0'})
response = urlopen(url).read()
currentHash = hashlib.sha224(response).hexdigest()
logging.info("running")

time.sleep(10)

while True:
    try:
        response = urlopen(url).read()
        currentHash = hashlib.sha224(response).hexdigest()
        time.sleep(10)
        response = urlopen(url).read()
        newHash = hashlib.sha224(response).hexdigest()
        if newHash == currentHash:
            continue
        else:
            app.send_message(-1001330957197,"something changed")
            response = urlopen(url).read()
            currentHash = hashlib.sha224(response).hexdigest()
            time.sleep(10)
            continue
    except Exception as e:
        app.send_message(-1001330957197,"error")
        continue
idle()