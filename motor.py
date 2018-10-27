import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)


p1 = GPIO.PWM(3,80)
p2 = GPIO.PWM(6,80)


p1.start(0)
p2.start(0)

def speed_1(s):
    p1.ChangeDutyCycle(s)

def speed_2(s):
    p2.ChangeDutyCycle(s)


if __name__ == '__main__':

    while True:
        speed(90)
        time.sleep(3)
        speed(10)
        time.sleep(3)
    
