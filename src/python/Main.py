import time
import Mail
from PIL import Image, ImageDraw, ImageFont

import detect as detect_person

emailDst="jeduartea@unal.edu.co"
image_name = "./data/images/surveillance2.png"
# surveillance1.png has no people
# surveillance2-4.png have people
iou_threshold = 0.5
confidence_threshold = 0.7

def main():
    while isSignal():
        img = getPhoto()
        if(hasPerson(img)):
            sendMail(emailDst, image_name)
            break

def isSignal():
    time.sleep(30)
    return True

def getTemp():
    return 0

def getProx():
    return 0

def getPhoto():
    return Image.open(image_name)

def hasPerson(img):
    return detect_person.main("images", iou_threshold, confidence_threshold, img)

def sendMail(emailDst, dirPhoto):
    Mail.sendMail(emailDst, dirPhoto)

main()

##############################3
#
#
#
