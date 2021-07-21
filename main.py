from mctools import RCONClient
from threading import Thread
import os
import re

HOST = os.environ.get('SERVER-IP')
PORT = os.environ.get('SERVER-PORT')
PASSWORD = os.environ.get('SERVER-PASSWORD')
rcon = RCONClient(HOST, port=int(PORT))



def rc(send):
    if rcon.login(PASSWORD):
            global get
            get = rcon.command(send, return_packet=True)
            get = re.sub(r'\x1B[@A-Z\\\]^_]\|\x1B\[[0-9:;<=>?]*[-!"#$%&'"'"'()*+,.\/]*[][\\@A-Z^_`a-z{|}~]', '', str(get))
            return get
        

