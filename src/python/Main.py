import time
from PIL import Image, ImageDraw, ImageFont
from servicesh import ServiceSh
import detect as detect_person

emailDst="coreo@gmail.com"
image_name = "./data/images/surveillance1.png"
# surveillance1.png has no people
# surveillance2-4.png have people
iou_threshold = 0.5
confidence_threshold = 0.7

def main():
   while True:
    while isSignal():
        img = getPhoto()
        if(hasPerson(img)):
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
    return Image.open(image_name)

def hasPerson(img):
    return detect_person.main("images", iou_threshold, confidence_threshold, img)

def sendMail():
    print("Sending mail..")

main()

##############################3
#
#
#

