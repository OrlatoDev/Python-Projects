import socket
from tkinter import *

hostname = socket.gethostname()

Ip = socket.gethostbyname(hostname)

window = Tk()

window['bg'] = "black"
window.geometry("400x350")
window.title("Get IP Address for PC: "+str(hostname))

def btn_Clicked():
    iplabel['text'] = "IP for PC: "+str(hostname)+": "+str(Ip)
    iplabel.pack(side=TOP, pady=30, fill=BOTH)

title = Label(window, text="IP Address", font="Helvetica 20", bg="black", fg="white")
title.pack(side=TOP, pady=30)

btn = Button(window, text="Get IP", relief=FLAT, bg="Gray9", fg="white", font="Helvetica 9", width=15, command=btn_Clicked)
btn.pack()

iplabel = Label(window, bg="black", fg="white", relief=FLAT, font="Helvetica 9", justify=CENTER)

window.mainloop()