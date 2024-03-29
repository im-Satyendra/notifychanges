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
        bot_token=":",
        api_id=1612723,
        api_hash="",
    )
app.start()
logging.info("Starting Assistant...")
logging.info("𝑨𝒔𝒔𝒊𝒔𝒕𝒂𝒏𝒕 𝒉𝒂𝒔 𝒃𝒆𝒆𝒏 𝒔𝒕𝒂𝒓𝒕𝒆𝒅 𝒔𝒖𝒄𝒄𝒆𝒔𝒔𝒇𝒖𝒍𝒍𝒚")
ttkn = ""
tsid = ""
tphno = "+"

TWILIO_ACCOUNT_SID = tsid
TWILIO_AUTH_TOKEN = ttkn 
TWILIO_PHONE_SENDER = tphno # replace with the phone number you registered in twilio
TWILIO_PHONE_RECIPIENT = "+" # replace with your phone number
cli = tc(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

app.send_message(-1001330957197,"started")
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
PrevVersion = ""
FirstRun = True
while True:
   try:
    url = "https://jeemain.nta.nic.in"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    for script in soup(["script", "style"]):
        script.extract() 
    soup = soup.get_text()
    if PrevVersion != soup:
        if FirstRun == True:
            PrevVersion = soup
            FirstRun = False
            app.send_message(-1001330957197,"Start Monitoring "+url+ ""+ str(datetime.now()),disable_notification=True)
        else:
            app.send_message(-1001330957197,"Changes detected at: "+ str(datetime.now()))
            OldPage = PrevVersion.splitlines()
            NewPage = soup.splitlines()
            d = difflib.Differ()
            diffone = d.compare(OldPage, NewPage)
            out_textone = "\n".join([ll.rstrip() for ll in '\n'.join(diffone).splitlines() if ll.strip()])
            preoneo = (out_textone)
            pretwoo = ('\n'.join(diffone))
            chngso = f"{preoneo}\n{pretwoo}"
            diff = difflib.context_diff(OldPage,NewPage,n=10)
            out_text = "\n".join([ll.rstrip() for ll in '\n'.join(diff).splitlines() if ll.strip()])
            preone = (out_text)
            pretwo = ('\n'.join(diff))
            chngs = f"{preone}\n{pretwo}"
            app.send_message(-1001330957197,str(str(f'{chngso}').replace('*',' ').replace('-',' ').replace('_',' ')))
            app.send_message(-1001330957197,str(str(f'{chngs}').replace('*',' ').replace('-',' ').replace('_',' ')))
            bth1 = str(str(f'{chngso}').replace('*',' ').replace('-',' ').replace('_',' '))
            bth2 = str(str(f'{chngs}').replace('*',' ').replace('-',' ').replace('_',' '))
            altxt = f"{bth1}\n{bth2}"
            cli.messages.create(
        to=TWILIO_PHONE_RECIPIENT,
        from_=TWILIO_PHONE_SENDER,
        body=altxt)
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
