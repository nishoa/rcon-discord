from mctools import RCONClient
from threading import Thread

HOST = '135.181.170.93'
PORT = 25623

rcon = RCONClient(HOST, port=PORT)


def rc(send):
    if rcon.login('Kpl9jdhJ'):
            rcon.command(send)

