from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import subprocess
from os import chdir


class side_panel_local():
    def __init__(self, window):
        self.window = window

        # Create buttons
        self.change_to_remote = Button(self.window, text="Switch to remote Host")
        self.change_to_remote.grid(column=0, row=1)

        # Get avalon version and branch to work in
        self.ask_version_avalon = Label(window, text='Enter the Realese of avalon')
        self.ask_version_avalon.grid(column=0, row=0, columnspan=2)
        global version
        self.version_combobox = Combobox(window, textvariable=version, state='readonly')
        self.version_combobox['values'] = ('Latest', '0.6', '0.5')
        self.version_combobox.current(0)
        self.version_combobox.grid(column=2, row=0)


class super_class:
    def __init__(self, window):

        global version

        # Define variables
        self.window = window

        # Get path to avalon from user
        self.ask_avalon_path = Label(window, text='Enter the path to avalon')
        self.ask_avalon_path.grid(column=0, row=0)
        self.path_to_avalon = Label(window, width=50, background='grey')
        self.path_to_avalon.grid(column=1, row=0, sticky='e', columnspan=1000)
        self.browse_avalon = Button(window, text="Browse to avalon", command=self.browse_to_avalon)
        self.browse_avalon.grid(column=1002, row=0)

        self.rebase_avalon = Button(window, command=lambda: self.configure_avalon(release=version.get()), text="Validate Repository")
        self.rebase_avalon.grid(row=2, column=0, sticky='w')

    def browse_to_avalon(self):
        avalon = filedialog.askdirectory()
        self.path_to_avalon.configure(text=avalon)

    def configure_avalon(self, **kwargs):
        global commit_id
        branch = kwargs.get('branch', None)
        release = kwargs.get('release', None)
        if branch == None:
            branch = 'master'
        if release == None:
            release = 'Latest'
        print(self.path_to_avalon.cget("text"))
        chdir(self.path_to_avalon.cget("text"))
        try:
            a = subprocess.check_output("git stash")
        except:
            pass
        try:
            a = subprocess.check_output("git rebase --abort")
        except:
            pass
        a = subprocess.check_output("git fetch https://github.com/hyperledger/avalon.git && git rebase -X ours", shell=True)
        if release == 'Latest':
            commit_id = subprocess.check_output("git ls-remote https://github.com/hyperledger/avalon.git refs/heads/master", shell=True)
            commit_id = commit_id.decode('UTF-8')
            commit_id = commit_id.split('\t', 1)
            commit_id = commit_id[0]
        if release == '0.5':
            commit_id = '1b543012f7b9f06508f0236ba044b640f89d1583'
        if release == '0.6':
            commit_id = 'cde34ee441df6d34d02addca9255c0b6bed9da8e'
        subprocess.check_output("git reset --hard " + commit_id, shell=True)


main = Tk()
main.title('Avalon Gui')
main.resizable(0, 0)

version = StringVar()

side_panel = Frame(main)
side_panel.grid(column=0, row=0)
side_panel_local(side_panel)

panel_divider = Canvas(main, width=5)
panel_divider.create_line(5, 10, 5, 500, fill='red')
panel_divider.grid(row=0, column=1, rowspan=500)

local_main = Frame(main)
local_main.grid(column=3, row=0)
super_class(local_main)

main.mainloop()
