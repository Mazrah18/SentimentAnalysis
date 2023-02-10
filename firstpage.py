from tkinter import *
from PIL import ImageTk,Image

class FirstPage:
    def __init__(self,root):
        self.root=root
        self.f = Frame(self.root, width=1500, height=1000)
        #self.f.pack()
        self.img = ImageTk.PhotoImage(Image.open("sentiment1.jpg"))
        self.panel = Label(self.f, image=self.img)
        self.panel.pack()
        self.m = Message(self.f, width=600, font="Roman 20 bold italic",
                            text="Feedback", bg="white", relief=SOLID
                            , borderwidth=2)
        self.m.place(x=600, y=40)
        self.panel.pack_propagate(0)
        self.f.pack_propagate(0)
#root=Tk()
#d=FirstPage(root)
#root.mainloop()
