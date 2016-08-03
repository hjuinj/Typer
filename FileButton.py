# -*- coding: utf-8 -*- 
import os
from Tkinter import *
from tkFileDialog import askopenfilename

class FileButton(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.loadFile()
        self.initUI() 
        
        
    def initUI(self):
        self.parent.title("FileButton")
        self.pack(fill = BOTH, expand=True)
        
        frame = Frame(self)
        frame.pack(fill=X)
        self.select = Button(self, text = "Select File")
        self.select.bind("<Button-1>", self.selectFile)
        
        self.select.pack(side = LEFT, padx = 5, pady = 5)

        
    def selectFile(self, event):
        filename = askopenfilename() 
        self.document = "".join(open(filename, "r").readlines())
        self.i = 0 
        
    def loadFile(self):
        #Read Text File
        try:
            path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "MidnightsDream_Shakes.txt")
        except NameError:  # We are the main py2exe script, not a module
            import sys
            path = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), "MidnightsDream_Shakes.txt")

        # path = os.path.join(os.path.dirname(__file__), "MidnightsDream_Shakes.txt")
        text_file = open(path,  "r")
        self.document = "".join(text_file.readlines())
        self.i = 0 
        text_file.close()



if __name__ == '__main__':
    root = Tk()
    app = FileButton(root)
    root.mainloop()
