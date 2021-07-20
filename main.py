from mctools import RCONClient
from threading import Thread

HOST = 'SERVER-IP'
PORT = 'SERVER-PORT'
print(PORT)
rcon = RCONClient(HOST, port=int(PORT))


def rc(send):
    if rcon.login('SERVER-PASSWORD'):
            rcon.command(send)

