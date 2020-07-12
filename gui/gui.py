from tkinter import *
from tkinter import filedialog


class side_panel_local():
    def __init__(self, window):
        self.window = window

        # Create buttons
        self.change_to_remote = Button(self.window, text="Switch to remote Host")
        self.change_to_remote.grid(column=0, row=0)


class work_on_local:
    def __init__(self, window):

        # Define variables
        self.window = window

        # Get path to avalon from user
        self.path_to_avalon = Label(window, width=50, background='grey')
        self.path_to_avalon.grid(column=0, row=0, sticky='e')
        self.browse_avalon = Button(window, text="Browse to avalon", command=self.browse_to_avalon)
        self.browse_avalon.grid(column=1, row=0)
    

    def browse_to_avalon(self):
        avalon = filedialog.askdirectory()
        if avalon != NONE:
            self.path_to_avalon.configure(text=avalon)


main = Tk()
#main.geometry(300)
main.resizable(0, 0)

side_panel = Frame(main)
side_panel.grid(column=0, row=0)
a = side_panel_local(side_panel)

panel_divider = Canvas(main, width=5)
panel_divider.create_line(5, 10, 5, 500, fill='red')
panel_divider.grid(row=0, column=1)

local_main = Frame(main)
local_main.grid(column=3, row=0)
b = work_on_local(local_main)


main.mainloop()
