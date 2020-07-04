import time

from servicesh import ServiceSh

emailDst="coreo@gmail.com"


def main():
   while True:
    while isSignal():
       potho=getPhoto()
       if(hasPerson(potho)):
           sendMail()
    time.sleep(0.3)

def isSignal():
    service = ServiceSh()
    return service.isSignal()

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

