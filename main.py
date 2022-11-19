import os, asyncio, geocoder
from cryptography.fernet import Fernet
global ip
ip = geocoder. ip("me")
#modules
def genkey():
    ekey = Fernet.generate_key()
    yn=input("Do you want to overwrite previous key? Y/N :")
    if yn == "Y":
        os.system("del C:\Windows\System32\BMR")
        ekeysave = open("C:\Windows\System32\BMR", "a")
        ekeysave.write(str(ekey))
        ef= Fernet(ekey)
    else:
        pass
    if yn == "y":
        os.system("del C:\Windows\System32\BMR")
        ekeysave = open("C:\Windows\System32\BMR", "a")
        ekeysave.write(str(ekey))
        ef= Fernet(ekey)
    else:
        pass
    return

def getkey():
    with open ("C:\Windows\System32\BMR", "r") as dkeysave:
        dkey = dkeysave.read()
    print(bytes(dkey, encoding='utf8'))
    global df
    df= Fernet(dkey)
    return
def encrypt():
    s = False
    if not s:
        try:
            genkey()
            getkey()
            file=input("Specify file :")
            with open(file, "r") as toread:
                reading = toread.read()
            print(reading)
            filee=df.encrypt(bytes(reading, encoding="utf8")) 
            #file + encrypt = file*e*
            filees=open(file, "w")
            filees.write(str(filee))
            #file + encrypt = file*e* filee + save = filee*s*
            s = True
        except:
            pass
def decrypt():
    print("currently not working")
    getkey()
    s = False
    if not s:
        try:
            file=input("Specify file: ")
            with open(file, "r") as toread:
                reading = toread.read()
            print(reading)
            filed=df.decrypt(reading) 
            #file + decrypt = file*d*
            fileds=open(file, "w")
            fileds.write(str(filed) - ".asp")
            #file + encrypt = file*e* filee + save = filee*s*
        except:
            pass



class main():
    #startup
    def search():
        cmd = input("trshx@" + ip.ip + ":")
        
        if cmd == "help":
            print("Copyright DarkJester 2022")
        elif cmd == "encrypt":
                encrypt()
        elif cmd == "decrypt":
            decrypt()
        else:
            os.system(cmd)
    while True:
        search()

while True:
    main()
