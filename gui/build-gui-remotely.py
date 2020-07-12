from tkinter import *
from os import system

window = Tk()


Label(window, text='Please enter your IP : ').grid(row=0, column=0)
Label(window, text='Please enter your username : ').grid(row=1, column=0)

ip = Entry(window)
ip.grid(row=0, column=1)

user = Entry(window)
user.grid(row=1, column=1)

def check_connect(ip, user):
    system("./run_on_remote.sh " + user + " " + ip + " ls")

connect = Button(text='Check connectivity', command=lambda: check_connect(ip.get(), user.get()))
connect.grid(row=2, column=0)

window.mainloop()
