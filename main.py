import asyncio
import os
import uvloop
import sys

if not os.getenv('DEVICE_ID') and \
        not os.getenv('ACCOUNT_ID') and \
        not os.getenv('SECRET'):
   print("Please paste your device auths into the \".env\" file. \n"
         "If you're confused, re-watch the tutorial.")
   sys.exit()
   
os.system('pip install -U SouvloBotPackage==0.0.6')
os.system('clear')

import SouvloBotPackage

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

client = SouvloBotPackage.SouvloBot(
     device_id=os.getenv('DEVICE_ID'),
     account_id=os.getenv('ACCOUNT_ID'),
     secret=os.getenv('SECRET')
)

try:
     client.run()
except Exception as e:
    print(e)
    print("Failed to login, your device auths are probably invlid, please "
          "try again and make new ones.\nIf you're confused, re-watch the "
          "tutorial.")
