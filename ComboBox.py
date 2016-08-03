# -*- coding: utf-8 -*- 

from Tkinter import *
from ttk import Combobox

class ComboBox(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
        self.speed = 1.0

    def initUI(self):
        self.parent.title("Combobox")
        self.pack(fill = BOTH, expand=True)
        frame = Frame(self)
        frame.pack(fill=X)
        
        field = Label(frame, text = "Typing Speed:", width = 15)
        field.pack(side = LEFT, padx = 5, pady = 5)
        
        self.box_value = StringVar()
        self.box = Combobox(frame, textvariable=self.box_value, width = 5)
        self.box['values'] = ('1x', '2x', '5x', '10x' )
        self.box.current(0)
        self.box.pack(fill = X, padx =5, expand = True)
        self.box.bind("<<ComboboxSelected>>", self.value)
        

    def value(self,event):
        self.speed =  float(self.box.get()[:-1])
    
if __name__ == '__main__':
    root = Tk()
    app = ComboBox(root)
    root.mainloop()
