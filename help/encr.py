from cryptography.fernet import Fernet
import os

def encrypt(path):
    if not os.path.exists("encrypt"):
        os.makedirs("encrypt")
    mkey()
    exec(path)

def exec(path):
    with open('encrypt/.keyencr', 'rb') as keys:
        key = keys.read()
        fernet = Fernet(key)
    with open(path, 'rb') as file:
        oris = file.read()
        encr = fernet.encrypt(oris)
    with open(path+".encr", 'wb') as encryped:
        encryped.write(encr)

def mkey():
    key = Fernet.generate_key()
    with open('encrypt/.keyencr', 'wb') as keys:
        keys.write(key)