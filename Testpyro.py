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
urls1 = "https://testservices.nic.in"
urls2= "https://examinationservices.nic.in"
urls3 = "https://satyendra.tech/"
urls4 = "https://testservices.nic.in/ExaminationServices/"
urls5 = "https://jeemain.nta.nic.in"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
def check(url):
 PrevVersion = ""
 FirstRun = True
 while True:
   try:
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
            OldPage = NewPage
            PrevVersion = soup
    else:
        logging.info(-1001330957197,"No Changes "+ str(datetime.now()))
    time.sleep(5)
    continue
   except Exception as e:
     print(e)
     continue
async def url1():
    print("ID of process running worker1: {}".format(os.getpid()))
    await check(urls1)
def url2():
    print("ID of process running worker2: {}".format(os.getpid()))
    check(urls2)
def url3():
    print("ID of process running worker3: {}".format(os.getpid()))
    check(urls3)
def url4():
    print("ID of process running worker4: {}".format(os.getpid()))
    check(urls4)
def url5():
    print("ID of process running worker5: {}".format(os.getpid()))
    check(urls5)
if __name__ == "__main__": 
    print("ID of main process: {}".format(os.getpid())) 
    p1 = multiprocessing.Process(target=url1) 
    p2 = multiprocessing.Process(target=url2)
    p3 = multiprocessing.Process(target=url3)
    p4 = multiprocessing.Process(target=url4)
    p5 = multiprocessing.Process(target=url5)
    p1.start() 
    p2.start()
    p3.start()
    p4.start()
    p5.start()
idle()