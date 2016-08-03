# -*- coding: utf-8 -*- 
from Tkinter import *
# from ttk import Frame, Button, Style, Scrollbar 

class TypingField(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        
        self.submit_tog = True
        self.initUI()
        self.text.bind_class("Text","<Control-a>", self.selectall)
        
    def initUI(self):
        self.parent.title("Text Field")
        self.pack(fill = BOTH, expand=True)
        
        frame1 = Frame(self.parent, width = 50, height =25)
        frame1.pack(fill = X, expand=True)
        self.scroll = Scrollbar(frame1)
        self.scroll.pack(side = "right", fill = Y)
        self.text = Text(frame1)
        self.text.pack(fill=Y)
        self.scroll.config(command=self.text.yview)
        self.text.config(yscrollcommand=self.scroll.set)
        
        
        frame2 = Frame(self.parent)
        frame2.pack(fill=X, expand=True)
        self.submit = Button(frame2,text="Start Test")
        self.submit.bind("<Button-1>", self.startPause)
        self.submit.pack(fill=X)
        
    def startPause(self, event):
        self.text.focus_set()
        if self.submit_tog:
            self.submit.configure(text = "Pause")
        else:
            self.submit.configure(text = "Start Test")
        self.submit_tog = not self.submit_tog
        
    def selectall(self, event):
        event.widget.tag_add("sel","1.0","end")
    
        
if __name__ == '__main__':
    root = Tk()
    app = TypingField(root)
    root.mainloop()
