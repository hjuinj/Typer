# -*- coding: utf-8 -*- 

from Tkinter import *
from ttk import Frame, Style, Combobox, Label

class ComboBox(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Combobox")
        self.pack(fill = BOTH, expand=True)
        frame = Frame(self)
        frame.pack(fill=X)
        
        field = Label(frame, text = "Typing Speed:", width = 15)
        field.pack(side = LEFT, padx = 5, pady = 5)
        
        self.box_value = StringVar()
        box = Combobox(frame, textvariable=self.box_value, width = 5)
        box['values'] = ('1x', '2x', '5x', '10x')
        box.current(0)
        box.pack(fill = X, padx =5, expand = True)
        

if __name__ == '__main__':
    root = Tk()
    app = ComboBox(root)
    root.mainloop()
