from Typer import *
from Prompt import *
import Tkinter as tk
from tkFileDialog import askopenfilename
import threading 
import Queue
import os

"""
TODO: move UI stuff into one single function
"""

class TextCanvas(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.master = parent
        self.promptDialog()
        self.setUI() 
        
        self.loadFile()
        self.sleepTime = 0.01
        
        if self.dialog.var.get() == 0:
            self.tw = TypeWriter()
        else:
            self.tw = TypeWriter(layout = "UK")
        
        self.periodicCall()
        
    def setUI(self):
        self.master.wm_attributes("-topmost", 1)

        # create a prompt, an input box, an output label,
        # and a button to do the computation
        self.master.title("SafeScribe")
        try:
            path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "SSicon.ico")
        except NameError:  # We are the main py2exe script, not a module
            import sys
            path = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), "SSicon.ico")
        self.master.wm_iconbitmap(path)
        self.text = tk.Text(self)
        self.submit = tk.Button(self, text="Start Test")
        self.submit_tog = True
        self.submit.bind("<Button-1>", self.startPause)
        self.scroll = tk.Scrollbar(self)
        self.select = tk.Button(self, text = "Select File")
        self.select.bind("<Button-1>", self.selectFile)
        # self.prompt = tk.Label(self, text="Speed:", anchor="w")
        # self.output = tk.Label(self, text="")

        # self.prompt.pack(side="top", fill="x")
        self.scroll.pack(side = "right", fill = "y")
        self.text.pack(side="top", fill="both", padx=40)
        self.select.pack(side="left")
        self.submit.pack(side="top")
        # self.output.pack(side="top", fill="x", expand=True)
        
        self.text.config(yscrollcommand=self.scroll.set)
        self.scroll.config(command=self.text.yview)
        self.master.wm_protocol("WM_DELETE_WINDOW", self.terminate)
        
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
        
    def promptDialog(self):
        self.dialog = Prompt(self.master)
        self.master.wait_window(self.dialog.top)
        
    def terminate(self):
        self.submit_tog = not self.submit_tog
        self.master.destroy()
        
    def periodicCall(self):
        self.master.after(100, self.periodicCall)
        
    ### Special Functions ###
    def allPermu(self, length, text = ""):
        if(length == 0):
            for i in text:
                self.tw.keyIn(i)
                time.sleep(sleepTime)
            self.tw.keyIn("ENTER")
            time.sleep(sleepTime)
        else:
            for i in self.tw.testString:
                if self.submit_tog:
                    return
                self.allPermu(length - 1,text+i, sleepTime)
                
    def randWords(self, length, text = ""):
        if(length == 0):
            for i in text:
                self.tw.keyIn(i)
                time.sleep(self.sleepTime)
            self.tw.keyIn(" ")
            for i in text:
                self.tw.keyIn(i.upper())
                time.sleep(self.sleepTime)
            self.tw.keyIn(" ")
            
            self.tw.keyIn(text[0].upper())
            time.sleep(self.sleepTime)
            for i in text[1:]:
                self.tw.keyIn(i)
                time.sleep(self.sleepTime)
            self.tw.keyIn("ENTER")
            time.sleep(self.sleepTime)
        else:
            for i in self.tw.testLetters:
                if self.submit_tog:
                    return
                self.randWords(length - 1,text+i, self.sleepTime)
    def workerThread(self):
        # self.randWords(4)
        # self.allPermu(3)
        self.runFile()
        
    
    ### Run threading 
    def runFile(self):
        while not self.submit_tog:
#             if self.focus_get() != self.text:
#                 self.submit_tog = True
#                 self.submit.configure(text = "Start Test")
#                 break
                
            if len(self.document) > self.i:
                self.tw.keyIn(self.document[self.i])
                self.i += 1
                time.sleep(self.sleepTime)
                
            else:
                self.tw.keyIn("\n")
                self.tw.CtrlA()
                self.tw.keyIn("BACK")
                self.i = 0
                # self.submit_tog = True
#                 self.submit.configure(text = "Start Test")
#                 break
    
    def startPause(self, event):
        if self.submit_tog:
            self.submit.configure(text = "Pause")
            self.text.focus_set()
            #Async 
            self.thread = threading.Thread(target = self.workerThread)
            self.thread.start()
        else:
            self.submit.configure(text = "Start Test")
        self.submit_tog = not self.submit_tog
        
    def selectFile(self, event):
        self.submit.configure(text = "Start Test")
        self.submit_tog = True
        filename = askopenfilename() 
        self.document = "".join(open(filename, "r").readlines())
        self.i = 0 


# if this is run as a program (versus being imported),
# create a root window and an instance of our example,
# then start the event loop
if __name__ == "__main__":
    root = tk.Tk()
    TextCanvas(root).pack(fill="both", expand=True)
    root.mainloop()
