#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import commands

pum = 12
count = 5
print("____APP Started____")
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(pum, GPIO.OUT)
print(str(commands.getoutput("ls /var/isaax/project/")))
print(str(commands.getoutput("ps aux | grep app")))
print(count)
while True:
    GPIO.output(pum, True)
    #print(str(commands.getoutput("ls /var/isaax/project/")))
    #print("LED is ON!")
    time.sleep(count)
    GPIO.output(pum, False)
    #GPIO.output(11, False)
    #print("LED is OFF!")
    time.sleep(count)
    #print("_____SYSTEMCTL_____")
    #print(str(commands.getoutput("systemctl status isaax-agent.service")))
    #print("___________________")
    #print("_____app revesion_____")
    #print(str(commands.getoutput("ls /var/isaax/project/")))
    #print("______________________")
