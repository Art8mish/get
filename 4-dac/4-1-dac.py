import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setup(dac, GPIO.OUT)

def dec2bin(val):
    return [int(i) for i in bin(val)[2:].zfill(8)]

try:
    while(True):
        print("Enter dec num (0-255): ")
        str = input()

        if (str == "q"):
            break

        num = int(str)

        if (num < 255 and num >= 0):
            GPIO.output(dac, dec2bin(num))
        else:
            print("Wrong number/n")

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()






