import cv2, time, os, datetime, getpass
import tkinter
from PIL import Image, ImageTk
cam=cv2.VideoCapture(0)
img=None

def takePhotoDef():
    os.system("mkdir -p ~/Pictures/camera")
    name=f'/home/{getpass.getuser()}/Pictures/camera/'
    name+=str(datetime.datetime.now())
    name+='.png'
    cv2.imwrite(f"{name}", img)
    photoPathAndName['text']=name

def camLoop():
    global img
    _, img = cam.read()
    img = cv2.flip(img, 1)
    im =cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    im = Image.fromarray(im)
    imgtk = ImageTk.PhotoImage(image=im)
    label['image'] = imgtk
    label.update()
    time.sleep(0.03)
    root.after(0, camLoop)

_, img = cam.read()
img =cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
root = tkinter.Tk() 

root.title("Camera App By Abhay Vachhani")
im = Image.fromarray(img)
imgtk = ImageTk.PhotoImage(image=im) 

label = tkinter.Label(root, image=imgtk)
label.pack()
camLogo = tkinter.PhotoImage(file='camera.png') 
takePhotoBtn = tkinter.Button(root, text='Photo', command=takePhotoDef, image=camLogo, borderwidth=0, highlightthickness=0)
takePhotoBtn.pack()
takePhotoBtn.focus()
photoPathAndName = tkinter.Label(root, text='')
photoPathAndName.pack()
camLoop()
root.mainloop()