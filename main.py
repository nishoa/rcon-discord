from mctools import RCONClient
from threading import Thread
import os

HOST = os.environ.get('SERVER-IP')
PORT = os.environ.get('SERVER-PORT')
PASSWORD = os.environ.get('SERVER-PASSWORD')
rcon = RCONClient(HOST, port=int(PORT))



def rc(send):
    if rcon.login(PASSWORD):
            global get
            get = rcon.command(send, return_packet=True)
            return get
        

