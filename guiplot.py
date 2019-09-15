#!/usr/bin/python3


import matplotlib.pyplot as plt
import matplotlib.animation as animation
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from tkinter import *
 
window = Tk()

window.geometry('640x480') # window size

window.title("Welcome to GUI Plot App") # window title
 
lbl = Label(window, text="Clique para abrir o destino do arquivo (algozscore.txt)", font=("Arial Bold", 11)) # Text inside window
 
lbl.grid(column=0, row=0) # posição do label

def clicked(): # criar função para quando o botão for clicado
     Tk().withdraw()
     global data_file #criar variavel global, pode ser usada fora da função
     data_file = askopenfilename()
    
btn = Button(window, text="Abrir arquivo", bg="white", fg="blue", command=clicked) # criar botão/ command=função do botão
 
btn.grid(column=1, row=0) # posição do botão

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
    ax1.set_title(data_file)
    ax1.set_xticks(ax1.get_xticks()[::60])

lbl2 = Label(window, text="Clique para plotar o gráfico", font=("Arial Bold", 11)) # Text inside window
 
lbl2.grid(column=0, row=4) # posição do label

def plot():
    ani = animation.FuncAnimation(fig, animate, interval=1000)
    plt.show()

btn2 = Button(window, text="Plotar", bg="white", fg="blue", command=plot) # criar botão/ command=função do botão
 
btn2.grid(column=1, row=4) # posição do botão
 
window.mainloop() # need loop to maintain it open
