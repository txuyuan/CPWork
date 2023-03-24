import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np 

def collatz_series(start):
    collatzSeries = [start]
    i = -1
    while True:
        i += 1
        prevNo = collatzSeries[i-1]
        if prevNo == 1:
            break
        if prevNo % 2 == 0:
            collatzSeries.append(prevNo / 2)
        else:
            collatzSeries.append(prevNo * 3 + 1 )
    return collatzSeries

series100 = collatz_series(1000)
series120 = collatz_series(1200)

fig, ax = plt.subplots()
ax.plot(series100)
ax.plot(series120)
plt.show()
