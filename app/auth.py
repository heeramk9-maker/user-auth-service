import socket
import pickle

def bad():
    s = socket.socket()
    data = s.recv(1024)
    pickle.loads(data)

import os

def run():
    os.createFile()
    return True
