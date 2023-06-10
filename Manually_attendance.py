from tkinter import * # type: ignore
root = Tk()
root.config(bg = 'white')
root.state('zoomed')

f3 = Frame(root, bg= "white")
Label(f3,bg="black", text= 'Manually Attendence', fg="White",font=("Helvetica", 20),height=6).pack(fill=X)
f3.pack(fill=BOTH, expand=1)


root.mainloop()