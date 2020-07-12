from tkinter import *
from tkinter import filedialog
from threading import Thread
from paramiko import AutoAddPolicy, SSHClient


class test_connect():
    def __init__(self, window):

        self.window = window

        # Get ip from user
        self.ask_ip = Label(window, text="Please enter your hostname(ip)")
        self.ask_ip.grid(row=0, column=0, columnspan=1)
        self.ip = Entry(window)
        self.ip.grid(column=1, row=0)

        # get username from user
        self.ask_user = Label(window, text="Please enter your username")
        self.ask_user.grid(row=1, column=0, sticky=W)
        self.user = Entry(window)
        self.user.grid(column=1, row=1)

        # get password from user
        self.ask_passwd = Label(window, text="Please enter your password")
        self.ask_passwd.grid(row=3, column=0, sticky=W)
        self.passwd = Entry(window, show="*")
        self.passwd.grid(column=1, row=3)

        # Create variables
        self.auth = IntVar()
        self.key_path = ''

        self.auth.set(1)

        # Create Radio buttons
        self.passwd_button = Radiobutton(text='Password', variable=self.auth, value=1, command=self.auth_change)
        self.key_button = Radiobutton(text='SSH key', variable=self.auth, value=2, command=self.auth_change)

        self.passwd_button.select()

        self.passwd_button.grid(column=0, row=2, sticky=W)
        self.key_button.grid(column=0, row=4, sticky=W) 

        # Create error labels
        self.connect_check_error = Label(window, text="")
        self.connect_check_error.grid(column=0, row=6)

        # Create buttons
        self.check_connect_button = Button(window, text="Check connectivity", command=self.check_connect)
        self.check_connect_button.grid(row=7, column=0)

        self.file = Button(window, text="Browse", command=self.open_file)
        self.file.grid(column=0, row=5)

        self.next = Button(window, text="next", command=self.go_ahead, state="disabled")
        self.next.grid(row=7, column=1)

        self.auth_change()


    def check_connect(self):
        client = SSHClient()
        client.set_missing_host_key_policy(AutoAddPolicy())
        try:
            if self.auth.get() == 1:
                client.connect(hostname=self.ip.get(), username=self.user.get(), password=self.passwd.get())
            else: client.connect(self.ip.get(), username=self.user.get(), key_filename=self.key_path)
        except:
            self.connect_check_error.configure(text="Couldn't connect to remote!")
            self.next.configure(state='disabled')
        else:
            self.connect_check_error.configure(text="Connected")
            self.next.configure(state='normal')


    def open_file(self): 
        f = filedialog.askopenfile(mode ='r', filetypes =[("Ssh keys file", '*.ppk'), ("Ssh key file", ".pem")])
        if f is not None:
            self.key_path = f.name


    def auth_change(self):
        if self.auth.get() == 1:
            self.file.configure(state='disabled')
            self.passwd.configure(state='normal')
            return
        self.file.configure(state='normal')
        self.passwd.configure(state='disabled')


    def go_ahead(self):
        main = Tk()
        if self.auth.get() == 1: work = work_on_remote(main, ip=self.ip.get(), user=self.user.get(), auth=self.auth.get(), password=self.passwd.get())
        if self.auth.get() == 2: work = work_on_remote(main, ip=self.ip.get(), user=self.user.get(), auth=self.auth.get(), key=self.key_path)
        self.window.destroy()
        #main.mainloop()


class work_on_remote():
    def __init__(self, window, ip='', user='', auth=0, key=None, password=None):

        self.window = window

        self.avalon_path = ''
        self.avalon_version = 0.0
        
        self.get_avalon = Toplevel(self.window)
        self.set_path_avalon(self.get_avalon)
        self.get_avalon.grab_set()
        self.get_avalon.mainloop()
    
    
    def set_path_avalon(self, window):

        ask_path = Label(window, text="Please enter the path to avalon")
        ask_path.grid(column=0, row=0)
        
        path = Entry(window)
        path.insert(0, self.avalon_path)
        path.grid(column=1, row=0)
        
        ask_version = Label(window, text='Please enter the version of avalon')
        ask_version.grid(column=0, row=1)
        
        version = Entry(window)
        version.insert(0, self.avalon_version)
        version.grid(column=1, row=1)
        


test = Tk()
make_test = test_connect(test)

test.mainloop()