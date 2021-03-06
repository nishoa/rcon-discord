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
            get = re.sub(r'\x1B\[(;?[0-9]{1,3})+[mGK]', '', str(get))
            get = re.sub(r'^[R,\s]..[R,N].+\n', '', get, 0, re.MULTILINE)
            get = re.sub(r'^\s.{10}', '', get, 0, re.MULTILINE)
            return get
        

