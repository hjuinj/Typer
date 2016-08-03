from Tkinter import *

class Prompt:
    def __init__(self, parent):

        self.parent = parent
        self.var = IntVar()
        top = self.top = Toplevel(parent)
        self.top.attributes("-toolwindow",1)

        R1 = Radiobutton(top, text="US Keyboard", variable=self.var, value=0)
        R1.pack( anchor = W )
        
        R2 = Radiobutton(top, text="UK Keyboard", variable=self.var, value=1)
        R2.pack( anchor = W )
        
        
        self.label = Label(top).pack()
        self.button = Button(top, text = "OK", command=self.submit).pack()
        self.top.title("Keyboards")
        
    def submit(self):
        self.top.destroy()
        # print self.var.get()
        # return self.var.get()


if __name__ == "__main__":
    root = Tk()
    Button(root, text="Hello!").pack()
    root.update()
    
    d = Prompt(root)
    
    root.wait_window(d.top)
