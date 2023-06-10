import cv2
from cv2 import COLOR_RGB2BGR
from simple_facerec import SimpleFacerec
from datetime import datetime
from tkinter import * # type: ignore
from PIL import ImageTk, Image


# Load Camera
def face_reco():
    ret, frame = cap.read()

    # Detect Faces
    face_locations, face_names = sfr.detect_known_faces(frame)
    for face_loc, name in zip(face_locations, face_names):
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

        if name!="Unknown":
            cv2.putText(frame, name, (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (54, 240, 7), 1)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (54, 240, 7), 1)
        else:
            cv2.putText(frame, name, (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 1)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 1)

    bgrframe = cv2.cvtColor(frame,COLOR_RGB2BGR)
    # cv2.imshow("Frame", frame)
    img = Image.fromarray(bgrframe).resize((500,500))  # type: ignore
    imgtk = ImageTk.PhotoImage(image = img)
    l3.config(image=imgtk)
    l3.image = imgtk  # type: ignore
    with open("./Attendence Sheets/Attendence.csv", 'r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        for name in face_names:
            if name not in nameList:
                now = datetime.now()
                time = now.strftime('%I:%M:%S:%p')
                date = now.strftime('%d-%B-%Y')
                f.writelines(f'{name}, {time}, {date}\n')
    l3.after(10,face_reco)
    

root = Tk()
root.config(bg = 'white')
root.state('normal')

b2 = Button(root,text= "open webcam",command=face_reco)
b2.pack()
l3 = Label(root)
l3.pack()
sfr = SimpleFacerec()
# Encode faces from a folder
sfr.load_encoding_images("photos\\")
# cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap = cv2.VideoCapture(0)

# face_reco()
root.mainloop()