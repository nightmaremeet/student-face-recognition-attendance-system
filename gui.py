from tkinter import *
# from train_face_gui import train_face_gui
# from main_video import face_reco

def train_face_gui():
    pass

def face_reco():
    pass

def lstbox():
    with open("./Attendance.csv","r") as fs:
        for i in fs.readlines():
            lb.insert("end",f"{str(i)}")


root = Tk()
root.title("Testing")
# root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
root.configure(background="white")
lb = Listbox(root,setgrid=True,width=100,height=10)
b1 = Button(root,text= "Attendence Sheet", background="black",font=("Comic Sans MS", 15, "bold"), foreground="white",height=3,width=30,padx=20,pady=10, command=lstbox)
b1.grid(column=0,row=0)
b2 = Button(root,text= "Train Face", background="black",font=("Comic Sans MS", 15, "bold"), foreground="white",height=3,width=30,padx=20,pady=10, command=train_face_gui)
b2.grid(column=1,row=0)
b3 = Button(root,text= "Manual Attendance", background="black",font=("Comic Sans MS", 15, "bold"), foreground="white",height=3,width=30,padx=20,pady=10)
b3.grid(column=2,row=0)
b4 = Button(root,text= "Open Webcam", background="black",font=("Comic Sans MS", 15, "bold"), foreground="white",height=3,width=30,padx=20,pady=10, command=face_reco)
b4.grid(column=3,row=0)


lb.grid(row=2,columnspan=4,padx=10,pady=10, ipadx=10, ipady=10)

root.state('zoomed') 
root.mainloop()