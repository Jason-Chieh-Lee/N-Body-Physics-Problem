from tkinter import *


class Push_Button:
    def __init__(self, root, text, command, row, column, padx, pady):
        self.butt = Button(root, text=text, command=command)
        self.butt.grid(row=row, column=column, padx=padx, pady=pady)
