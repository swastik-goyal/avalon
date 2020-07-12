from tkinter import *
import paramiko


class test_connect:
    def __init__(self, window):
        # Get ip from user
        self.ask_ip = Label(window, text="Please enter your hostname(ip)")
        self.ask_ip.grid(row=0, column=0)
        self.ip = Entry(window)
        self.ip.grid(column=1, row=0)

        # get username from user
        self.ask_user = Label(window, text="Please enter your username")
        self.ask_user.grid(row=1, column=0)
        self.user = Entry(window)
        self.user.grid(column=1, row=1)

        # get password from user
        self.ask_passwd = Label(window, text="Please enter your password")
        self.ask_passwd.grid(row=2, column=0)
        self.passwd = Entry(window, show="*")
        self.passwd.grid(column=1, row=2)

        # Create error labels
        self.connect_check_error = Label(window, text="Couldn't connect to remote through ssh!")

        # Create buttons
        self.check_connect_button = Button(window, text="Check connectivity", command=self.check_connect)
        self.check_connect_button.grid(row=4, column=0)

    def check_connect(self):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            client.connect(hostname=self.ip.get(), username=self.user.get(), password=self.passwd.get())
            # if self.connect_check_error.grid_info() != []:
            #     self.connect_check_error.grid_forget()
        except:
            if self.connect_check_error.grid_info() == []:
                self.connect_check_error.grid(row=3, column=0)



test = Tk()
make_test = test_connect(test)
test.mainloop()
