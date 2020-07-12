from tkinter import *
from tkinter.ttk import Combobox
from tkinter import scrolledtext
import os
import threading

window = Tk()

window.title('avalon')


lab1 = scrolledtext.ScrolledText(window)
lab1.grid(column=0, row=3, columnspan=100)

c = ''

def build():

    def get_logs():
        while True:
            global c
            f = open('logs.txt', 'r+')
            #lab1.delete('1.0', 'end')
            d = f.readlines()
            if c != d:
                lab1.insert('end', d[len(c):])
                c = d
            #lab1.insert('end', f.readlines())
            f.close()


    def build():
        os.system('docker-compose -f ../docker-compose.yaml build > logs.txt')

    t1 = threading.Thread(target=build)
    t1.start()
    t2 = threading.Thread(target=get_logs)
    t2.start()



Label(window, text='Mode').grid(column=0, row=0)
Label(window, text='Mode').grid(column=1, row=0)
Label(window, text='Mode').grid(column=2, row=0)

build = Button(text='Build', command=build)
mode1 = StringVar()
mode2 = StringVar()
mode3 = StringVar()

mode1_op = Combobox(window, textvariable=mode1, width=10, state='readonly')
# .grid(column=0, row=1)
mode2_op = Combobox(window, textvariable=mode2, width=10, state='readonly')
# .grid(column=1, row=1)
mode3_op = Combobox(window, textvariable=mode3, width=10, state='readonly')
# .grid(column=2, row=1)
build.grid(column=0, row=2)

mode1_op['values'] = ('Ganache', 'Besu', 'Direct', 'fabric')
mode2_op['values'] = ('Hardware', 'Simulator')
mode3_op['values'] = ('Singleton', 'Pool')
mode1_op.current(2)
mode2_op.current(1)
mode3_op.current(0)
mode1_op.grid(column=0, row=1, sticky=W)
mode2_op.grid(column=1, row=1, sticky=W)
mode3_op.grid(column=2, row=1, sticky=W)

window.resizable(0, 0)

window.mainloop()

