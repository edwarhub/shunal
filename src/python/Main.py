import time
import Mail
from PIL import Image, ImageDraw, ImageFont
from servicesh import ServiceSh
import detect as detect_person

emailDst="jeduartea@unal.edu.co"
image_name = "./data/images/surveillance2.png"
# surveillance1.png has no people
# surveillance2-4.png have people
iou_threshold = 0.5
confidence_threshold = 0.7

def main():
   print("-------------------------------------------")
   print("IoT - Universidad Nacional de Colombia")
   print("SHUNAL v 1.0.1")
   print("-------------------------------------------")
   print("Runing service...")
   while True:
    while isSignal():
        print("Sensors signal : ok")
        img = getPhoto()
        if(hasPerson(img)):
            print("Sending E-mail to:"+emailDst)
            sendMail(emailDst, image_name)
            #break
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

def sendMail(emailDst, dirPhoto):
    Mail.sendMail(emailDst, dirPhoto)

main()

##############################3
#
#
#
