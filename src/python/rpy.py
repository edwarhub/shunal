from __future__ import print_function

import RPi.GPIO as GPIO
import time
import os

# Pin Number
PIN1 = 19
PIN2 = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(PIN2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    pin_status1 = GPIO.input(PIN1)
    pin_status2 = GPIO.input(PIN2)

    if pin_status1==1:
        print("PIN 1: On")
        os.system("ssh -i /opt/shunal/id_rsa_edwar_nodo0 edwar@192.168.0.4 \"echo ON > /tmp/shunal_prox.txt\"")
        #time.sleep(1)

    if pin_status2==1:
        print("PIN 2: On")
        os.system("ssh -i /opt/shunal/id_rsa_edwar_nodo0 edwar@192.168.0.4 \"echo ON > /tmp/shunal_temp.txt\"")
        #time.sleep(1)

    time.sleep(0.1)

GPIO.cleanup()