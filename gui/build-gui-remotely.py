import paramiko

window = Tk()


Label(window, text='Please enter your IP : ').grid(row=0, column=0)
Label(window, text='Please enter your username : ').grid(row=1, column=0)
pw = Entry(window)
pw.grid(row=2, column=0)

ip = Entry(window)
ip.grid(row=0, column=1)

user = Entry(window)
user.grid(row=1, column=1)

def check_connect(hostname, username, password):
    # initialize the SSH client
    client = paramiko.SSHClient()
    # add to known hosts
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname=hostname, username=username, password=password, timeout=10)
    except Exception as err:
        c = err
        Label(window, text="!Failed to connect to remote machine using ssh !").grid(row=4, column=0, columnspan=5)
    else:
        window.destroy()
        return
    stdin, stdout, stderr = client.exec_command("ls -al")
    print(stdout.read().decode())
    err = stderr.read().decode()
    if err:
        print(err)



connect = Button(text='Check connectivity', command=lambda: check_connect(ip.get(), user.get(), pw.get()))
connect.grid(row=3, column=0)

window.mainloop()
