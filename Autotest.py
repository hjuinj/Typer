# -*- coding: utf-8 -*- 
from Typer import *
from Prompt import *
from FileButton import *
from Tkinter import *
from ComboBox import *
from TypingField import *
from ttk import Frame, Label, Button, Style
import threading 

class Autotest(Frame):
    def __init__(self, parent):
        Frame.__init__(self,parent)
        self.parent = parent
        self.setUI()
        
    def loadLogo(self):
        try:
            path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "SSicon.ico")
        except NameError:  # We are the main py2exe script, not a module
            import sys
            path = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), "SSicon.ico")
        self.parent.wm_iconbitmap(path)
        
    def setUI(self):
        self.style = Style()
        # self.style.theme_use("default")
        self.loadLogo()
        
        
        a = ComboBox(self.parent)
        a.pack(side = RIGHT)
        b = FileButton(self.parent)
        b.pack(fill = X)
        self.parent.title("Autotest")
        
        c = TypingField(self.parent)
        c.pack(fill=X)
        c.text.focus_set()
        

if __name__ == "__main__":
    root = Tk()
    app = Autotest(root)
    root.mainloop()
