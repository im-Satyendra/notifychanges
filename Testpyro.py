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
import requests
from bs4 import BeautifulSoup
import difflib
import time
from datetime import datetime

# target URL
url = "https://satyendra.tech/"
# act like a browser
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

PrevVersion = ""
FirstRun = True
while True:

    # download the page
    response = requests.get(url, headers=headers)
    # parse the downloaded homepage
    soup = BeautifulSoup(response.text, "lxml")
    
    # remove all scripts and styles
    for script in soup(["script", "style"]):
        script.extract() 
    soup = soup.get_text()
    # compare the page text to the previous version
    if PrevVersion != soup:
        # on the first run - just memorize the page
        if FirstRun == True:
            PrevVersion = soup
            FirstRun = False
            app.send_message(-1001330957197,"Start Monitoring "+url+ ""+ str(datetime.now()),disable_notification=True)
        else:
            app.send_message(-1001330957197,"Changes detected at: "+ str(datetime.now()))
            OldPage = PrevVersion.splitlines()
            NewPage = soup.splitlines()
            # compare versions and highlight changes using difflib
            #d = difflib.Differ()
            #diff = d.compare(OldPage, NewPage)
            diff = difflib.context_diff(OldPage,NewPage,n=10)
            out_text = "\n".join([ll.rstrip() for ll in '\n'.join(diff).splitlines() if ll.strip()])
            app.send_message(-1001330957197,out_text)
            OldPage = NewPage
            #print ('\n'.join(diff))
            PrevVersion = soup
    else:
        print( "No Changes "+ str(datetime.now()))
    time.sleep(10)
    continue
idle()