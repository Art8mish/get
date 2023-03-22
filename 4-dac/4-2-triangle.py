import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setup(dac, GPIO.OUT)

def dec2bin(val):
    return [int(i) for i in bin(val)[2:].zfill(8)]

try:
    while(True):
        for i in range(255):
            GPIO.output(dac, dec2bin(i))
            time.sleep(0.005)
        for i in range(255, 0, -1):
            GPIO.output(dac, dec2bin(i))
            time.sleep(0.005)

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()