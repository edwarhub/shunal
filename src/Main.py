import time


emailDst="coreo@gmail.com"


def main():
    while isSignal():
        potho=getPhoto()
        if(hasPerson(potho)):
            sendMail()    

def isSignal():
    time.sleep(5)
    return True

def getTemp():
    return 0

def getProx():
    return 0

def getPhoto():
    return "File Potho"

def hasPerson(photo):
    return True

def sendMail():
    print("Sending mail..")

main()

##############################3
#
#
#

