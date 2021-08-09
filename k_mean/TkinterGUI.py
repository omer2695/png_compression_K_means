from tkinter import *
import easygui
from PIL import Image, ImageTk


def get_image_path():
    global img_up
    # Open file explorer and upload image
    image_path = easygui.fileopenbox()
    image_path = image_path.replace('\\', '\\\\')
    img2 = Image.open(image_path)
    # Check if the image is too big to fit on screen
    width, height = img2.size
    if width > 256 or height > 256:
        size = 256, 256
        img2.thumbnail(size, Image.ANTIALIAS)
    # Make the image compatible with tkinter
    img_up = ImageTk.PhotoImage(img2)
    # Push the image onto its "label"
    image_container['image'] = img_up
    # Make the compress button clickable
    compress_button['state'] = NORMAL


def clear_screen():
    image_container['image'] = ""
    compress_button['state'] = DISABLED
    compressed_image['image'] = ""


root = Tk()
root.title('K-Means PNG Compression')
root.iconbitmap("icon.ico")


# Building all the widgets
image_container = Label(root)
compressed_image = Label(root)
label = Label(root, text="Compress your PNG image with K-means!", font=(None, 20))
upload_image_button = Button(root, text="Upload an image", command=get_image_path)
compress_button = Button(root, text="Compress", state=DISABLED)
clear_button = Button(root, text="Clear", command=clear_screen)
exit_button = Button(root, text="Exit", command=root.quit)


# Size of the screen
root.geometry("700x700")


# Placing the widgets
label.place(relx=0.13)
image_container.place(relx=0.1, rely=0.1)
compressed_image.place(relx=-0.1, rely=0.1)
upload_image_button.place(relx=0.1, rely=0.9)
compress_button.place(relx=0.27, rely=0.9)
clear_button.place(relx=0.38, rely=0.9)
exit_button.place(relx=0.45, rely=0.9)


# Initiate the main loop
root.mainloop()
