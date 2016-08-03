# -*- coding: utf-8 -*- 
from Typer import *
from Prompt import *
from FileButton import *
from Tkinter import *
from ComboBox import *
from TypingField import *
from ttk import Combobox, Style
import threading 

class Autotest(Frame):
    def __init__(self, parent):
        Frame.__init__(self,parent)
        self.parent = parent
        self.setUI()
        if self.prompt.var.get() == 0:
            self.tw = TypeWriter("US")
        elif self.prompt.var.get() == 1:
            self.tw = TypeWriter("UK")
        
        self.periodicCall()
        
    def periodicCall(self):
        self.master.after(100, self.periodicCall)
    def workerThread(self):
        # self.randWords(4)
        # self.allPermu(3)
        self.runFile()
        
    
    ### Run threading 
    def runFile(self):
        while not self.text.submit_tog:
            try:
                if self.focus_get() != self.text.text:
                    self.text.submit_tog = True
                    self.text.submit.configure(text = "Start Test")
                    break
               
                if len(self.file.document) > self.file.i:
                    print "if"
                    self.sleepTime = 0.1/self.speed.speed
                    self.tw.keyIn(self.file.document[self.file.i])
                    self.file.i += 1
                    time.sleep(self.sleepTime)
                    
                elif len(self.file.document) == self.file.i:
                    self.tw.keyIn("\n")
                    self.tw.CtrlA()
                    self.tw.keyIn("BACK")
                    self.file.i = 0
                else:
                    print "else"
            except:
                print "exception"
                
    def setUI(self):
        self.style = Style()
        self.prompt = Prompt(self.parent)
        self.style.theme_use("default")
        self.loadLogo()
        
        self.speed = ComboBox(self.parent)
        self.speed.pack(side = RIGHT)
        self.speed.box.bind("<<ComboboxSelected>>", self.pause)
        self.file = FileButton(self.parent)
        self.file.pack(fill = X)
        
        self.text = TypingField(self.parent)
        self.text.pack(fill=X)
        self.text.submit.bind("<Button-1>", self.startPause)
        
        self.parent.title("Autotest")
        
    def pause(self, event):
        self.text.submit_tog = True
        # self.text.submit.configure(text = "Start Test")
        
        self.speed.value(event)
        self.text.text.focus_set()
        # self.text.submit_tog = False
        self.startPause(event)
    def startPause(self, event):
        self.text.startPause(event)
        if not self.text.submit_tog:
            self.thread = threading.Thread(target = self.workerThread)
            self.thread.start()
    def loadLogo(self):
        try:
            path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "SSicon.ico")
        except NameError:  # We are the main py2exe script, not a module
            import sys
            path = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), "SSicon.ico")
        self.parent.wm_iconbitmap(path)
        
if __name__ == "__main__":
    root = Tk()
    app = Autotest(root)
    root.mainloop()
