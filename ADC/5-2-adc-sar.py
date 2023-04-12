
import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)

dac    = [26, 19, 13, 6, 5, 11, 9, 10]
comp   = 4
troyka = 17


GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def dec2bin(a):
    return [int (elem) for elem in bin(a)[2:].zfill(8)]

def adc():
    k = 0
    for i in range(7, -1, -1):
        k += 2**i
        GPIO.output(dac, dec2bin(k))
        time.sleep(0.05)
        if GPIO.input(comp) == 0:
            k -= 2**i
    return k

try:            
    while True:
        i = adc()
        if i != 0:
            print(i, '{:.2f}v'.format(3.3 * i/256))
        
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()   
