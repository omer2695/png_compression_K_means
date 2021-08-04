import tkinter
from tkinter import *
import easygui


def get_image_path():
    global img_up
    image_path = easygui.fileopenbox()
    image_path = image_path.replace('\\', '\\\\')
    img_up = tkinter.PhotoImage(file=image_path)
    my_label['image'] = img_up


root = Tk()
root.title('K-Means PNG Compression')
root.iconbitmap("icon.ico")

my_label = Label(root)
uploadImageButton = Button(root, text="Upload an image", command=get_image_path)
compressButton = Button(root, text="Compress", state=DISABLED)


my_label.pack()
uploadImageButton.pack()
compressButton.pack()
root.geometry("500x500")
root.mainloop()
