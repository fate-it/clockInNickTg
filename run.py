from telethon import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest
import asyncio
from datetime import datetime
import pytz
import subprocess
import sys

api_id = 000000000 #enter your api_id
api_hash = '' #enter your api_hash
phone_number = '+11122345567' #your tel number
username = 'username' #enter your username
time_zone = 'Europe/Warsaw' #change your time_zone


client = TelegramClient('session_name', api_id, api_hash)


def get_time():
    current_time = datetime.now(pytz.timezone(time_zone))
    #current_date = current_time.strftime(f"%d.%m.%Y")
    hour = f'{current_time.hour:02}'
    minutes = f'{current_time.minute:02}'
    return f'{username}|{hour}:{minutes}' #{current_date}'


async def change_name(new_first_name):
    await client(UpdateProfileRequest(first_name=new_first_name))


async def main():
    RESET = 0
    old_time = get_time()
    while True:
        if old_time != get_time():
            old_time = get_time()
            async with client:
                await change_name(f'{old_time}')
            #print('Changed to: '+old_time)
            #await asyncio.sleep(57)
            RESET+=1
            if RESET == 60:
                await asyncio.sleep(55)
                subprocess.Popen([sys.executable, *sys.argv])
                sys.exit()
            await asyncio.sleep(57)
        #else:
            #print('Wait: '+old_time)
            #await asyncio.sleep(1)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
