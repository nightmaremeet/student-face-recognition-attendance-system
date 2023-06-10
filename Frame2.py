# Import required libraries
from tkinter import *
from PIL import ImageTk, Image

# Create an instance of tkinter window
win = Tk()
win.state("zoomed")
# Define the geometry of the window
f1 = Frame(win)
f2 = Frame(win)
f3 = Frame(win)
f4 = Frame(win)

# frame.place(anchor='center', relx=0.5, rely=0.5)

def train_faceBtn():
    img = ImageTk.PhotoImage(Image.open("testing.jpg").resize((win.winfo_screenheight()//4,win.winfo_screenwidth()//4)))
    label = Label(f1, image = img)
    label.place(x= 100, y= 100)
train_faceBtn()
f1.pack(fill=BOTH, expand=1)
win.mainloop()