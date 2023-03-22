import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(22, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
p2 = GPIO.PWM(22, 1000)
p10 = GPIO.PWM(10, 1000)


try:
    while(True):
        print("Enter shim q (0-100): ")
        str = int(input())
        p2.stop()
        p10.stop()
        

        if (str == "q"):
            break

        num = int(str)

        if (num < 100 and num >= 0):
            p2.start(num)
            p10.start(num)
            
        else:
            print("Wrong number/n")
    
    input('Press return to stop:')   # use raw_input for Python 2
    


finally:
    GPIO.output(2, 0)
    GPIO.output(10, 0)
    GPIO.cleanup()