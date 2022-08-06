import os
import time
import asyncio
import pyrogram
import logging
import time
import hashlib
from urllib.request import urlopen, Request
from pyrogram import idle
from multiprocessing import Pool
import multiprocessing
import requests
from bs4 import BeautifulSoup
import difflib
import time
from datetime import datetime
from twilio.rest import Client as tc

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler(
                        'log.txt'), logging.StreamHandler()],
                    level=logging.INFO)

logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.ERROR)

app = pyrogram.Client(
        "Notify me",
        bot_token="1963945108:AAFyo9bg2k4BImXsAHgghYg2bEkkdaiDe4g",
        api_id=1612723,
        api_hash="eb3bc0998f7a134318a6d5763e9d0d49",
    )
app.start()
logging.info("Starting Assistant...")
logging.info("𝑨𝒔𝒔𝒊𝒔𝒕𝒂𝒏𝒕 𝒉𝒂𝒔 𝒃𝒆𝒆𝒏 𝒔𝒕𝒂𝒓𝒕𝒆𝒅 𝒔𝒖𝒄𝒄𝒆𝒔𝒔𝒇𝒖𝒍𝒍𝒚")

app.send_message(-1001579836800,"started")
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
PrevVersion = ""
FirstRun = True
while True:
   try:
    url = "https://jeeadv.ac.in/"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    for script in soup(["script", "style"]):
        script.extract() 
    soup = soup.get_text()
    if PrevVersion != soup:
        if FirstRun == True:
            PrevVersion = soup
            FirstRun = False
            app.send_message(-1001579836800,"Start Monitoring "+url+ ""+ str(datetime.now()),disable_notification=True)
        else:
            app.send_message(-1001579836800,"Changes detected at: "+ str(datetime.now()))
            exit()
            OldPage = NewPage
            PrevVersion = soup
    else:
        logging.info("No Changes "+ str(datetime.now()))
    time.sleep(5)
    continue
   except Exception as e:
     print(e)
     continue
idle()
