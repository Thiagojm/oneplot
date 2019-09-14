#!/usr/bin/python3


import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.dates as mdates
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
data_file = askopenfilename() # show an "Open" dialog box and return the path to the selected file
plt.rcParams["figure.figsize"] = (17,7)
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    pullData = open(data_file,"r").read()
    dataArray = pullData.split('\n')
    xar = []
    yar = []
    for eachLine in dataArray:
        if len(eachLine)>1:
            x,y = eachLine.split(' ')
            xar.append(x)
            yar.append(float(y))
    ax1.clear()
    ax1.plot(xar,yar)
    ax1.tick_params(axis ='x', rotation = 45) 
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.gcf().autofmt_xdate()
plt.show()
