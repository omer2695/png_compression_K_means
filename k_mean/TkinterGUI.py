import time
import tkinter.ttk
from tkinter import *
import easygui
from PIL import Image, ImageTk
import compressions_k_means
import threading


def get_image_path():
    global img_up
    global image
    # Open file explorer and upload image
    image_path = easygui.fileopenbox()
    image_path = image_path.replace('\\', '\\\\')
    image = Image.open(image_path)
    # Check if the image is too big to fit on screen
    width, height = image.size
    if width > 256 or height > 256:
        size = 256, 256
        image.thumbnail(size, Image.ANTIALIAS)
    # Make the image compatible with tkinter
    img_up = ImageTk.PhotoImage(image)
    # Push the image onto its "label"
    image_container['image'] = img_up
    # Make the compress button clickable
    compress_button['state'] = NORMAL


def clear_screen():
    image_container['image'] = ""
    compress_button['state'] = DISABLED
    compressed_image['image'] = ""
    progress.stop()
    # stop open_compressed_image from running


def open_compressed_image(compress_image):
    global compressed_image_to_open

    progress.start(300)
    while compressed_image_string.is_alive():
        time.sleep(0.5)

    compressed_image_to_open = Image.open(compress_image[0])
    compressed_image_to_open = ImageTk.PhotoImage(compressed_image_to_open)
    compressed_image['image'] = compressed_image_to_open
    progress.stop()


def compress():
    result = ["null"]
    global compressed_image_string

    # send the image to the compression algorithm
    compressed_image_string = threading.Thread(target=compressions_k_means.compress, args=(image, result,))
    compressed_image_string.start()
    # Wait till the thread is finished running , The main thread is stuck
    # after its returned the name of the saved image as string show it on the screen next to the orig image
    threading.Thread(target=open_compressed_image, args=(result,)).start()


root = Tk()
root.title('K-Means PNG Compression')
root.iconbitmap("icon.ico")


# Building all the widgets
image_container = Label(root)
compressed_image = Label(root)
label = Label(root, text="Compress your PNG image with K-means!", font=(None, 20))
upload_image_button = Button(root, text="Upload an image", command=get_image_path)
compress_button = Button(root, text="Compress", state=DISABLED, command=compress)
clear_button = Button(root, text="Clear", command=clear_screen)
exit_button = Button(root, text="Exit", command=root.quit)
progress = tkinter.ttk.Progressbar(root, orient=HORIZONTAL, length=200, mode='indeterminate')
loading_label = Label(root, text="Loading...", fg="#2191fb")
k_means_label = Label(root, text="k-means:")
k_means_Entry = Entry(root, bd=5)


# Size of the screen
root.geometry("700x700")


# Placing the widgets
label.place(relx=0.13)
image_container.place(x=100, y=100)
compressed_image.place(x=500, y=100)
upload_image_button.place(x=180, y=600)
compress_button.place(x=330, y=600)
clear_button.place(x=430, y=600)
exit_button.place(x=500, y=600)
loading_label.place(x=300, y=680)
progress.place(x=250, y=650)
k_means_label.place(x=240, y=450)
k_means_Entry.place(x=300, y=450)


# Initiate the main loop
root.mainloop()
