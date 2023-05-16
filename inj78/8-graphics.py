from matplotlib import pyplot as plt
import numpy as np
from textwrap import wrap
import matplotlib.ticker as ticker

with open('settings.txt') as sttngs_f:
    settings = [float(i) for i in sttngs_f.read().split('\n')]


data = np.loadtxt('data.txt', dtype=int) * settings[1] #шаг по напряжениюя

data_time = np.array([i * settings[0] for i in range(data.size)]) #шаг по времени
fig, ax   = plt.subplots(figsize=(16, 9), dpi=600)

ax.axis([data_time.min(), data_time.max() + 2, data.min(), data.max() + 1])

#для x
ax.xaxis.set_major_locator(ticker.MultipleLocator(1))    #интервал основных делений
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.25)) #интервал вспомогательных делений

#для y
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))


ax.set_title("\n".join(wrap('Процесс заряда и разряда конденсатора в RC-цепочке V(t)', 60)), loc = 'center')

#сетка
ax.grid(which='major', color = 'pink')
ax.grid(which='minor', color = 'gray', linestyle = ':')

ax.set_ylabel("Напряжение, В")
ax.set_xlabel("Время, с")

ax.plot(data_time, data, color='black', linewidth=1, label = 'V(t)')
ax.legend(loc = 'right', fontsize = 15)

fig.savefig('graph.png')

