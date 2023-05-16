import RPi.GPIO as GPIO
import time
from matplotlib import pyplot as plt

GPIO.setmode(GPIO.BCM)

leds=[21, 20, 16, 12, 7, 8, 25, 24]
GPIO.setup(leds, GPIO.OUT)

dac=[26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT, initial=GPIO.HIGH)

comp=4
troyka=17 
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp,   GPIO.IN)

#снятие показаний с тройки
def adc():
    k = 0
    for i in range(7, -1, -1):
        k += 2**i
        GPIO.output(dac, dec2bin(k))
        time.sleep(0.005)
        if (GPIO.input(comp) == 0):
            k -= 2**i
    return k

def dec2bin(a):
    return [int (elem) for elem in bin(a)[2:].zfill(8)]

try:
    troyka = 0
    result = []
    time_start = time.time()
    count = 0

    while troyka < 256 * 0.25:
        troyka = adc()
        result.append(troyka)
        count += 1
        GPIO.output(leds, dec2bin(troyka))

    GPIO.setup(troyka,GPIO.OUT, initial=GPIO.LOW)

    while troyka > 256 * 0.25:
        troyka = adc()
        result.append(troyka)
        count += 1
        GPIO.output(leds, dec2bin(troyka))

    exp_time = time.time() - time_start

    with open('data.txt', 'w') as data_f:
        for i in result:
            data_f.write(str(i) + '\n')
    with open('settings.txt', 'w') as sttngs_f:
        sttngs_f.write(str(1 / exp_time / count) + '\n')
        sttngs_f.write('0.01289')
    
    print('Общая продолжительность эксперимента {}\n'
          'Период одного измерения {}\n'
          'Средняя частота дискретизации {}\n'
          'Шаг квантования АЦП {}'.format(exp_time, exp_time/count, 1/exp_time/count, 0.01289))


    y=[i / 256 * 3.3 for i in result]
    x=[i * exp_time / count for i in range(len(result))]
    plt.plot(x, y)
    plt.xlabel('Time, s')
    plt.ylabel('Voltage, v')
    plt.savefig('plot1.png')

finally:
    GPIO.output(leds, 0)
    GPIO.output(dac, 0)
    GPIO.cleanup()