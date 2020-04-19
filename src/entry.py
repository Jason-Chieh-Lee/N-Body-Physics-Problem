from tkinter import *


class Text_Entry:
    def __init__(self, root, value, row, column, padx, pady):
        self.entry = Entry(root)
        self.entry.grid(row=row, column=column, padx=padx, pady=pady)
        self.entry.insert(0, value)

    def get_value(self):
        return self.entry.get()

    def set_value(self, value):
        self.entry.delete(0, 'end')
        self.entry.insert(0, value)
