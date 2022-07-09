import RPi.GPIO as GPIO
import time

pin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pin, GPIO.OUT)
p = GPIO.PWM(pin, 50)
p.start(0)
p.ChangeDutyCycle(2.5)

while True:
    p.ChangeDutyCycle(2.5)
    #print("0~")
    time.sleep(1)
    p.ChangeDutyCycle(9.5)
    #print("180~")
    time.sleep(1)
    
