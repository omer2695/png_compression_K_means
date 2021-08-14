import time
import tkinter.ttk
from tkinter import *
from tkinter import messagebox
import easygui
from PIL import Image, ImageTk
import compressions_k_means
import threading
import os


def get_image_path():
    clear_screen()
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


    image_details['text'] = ""
    compressed_image_details['text'] = ""
    compress_ratio_details['text'] = ""
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
    clear_button['state'] = NORMAL
    upload_image_button['state'] = NORMAL
    compress_button['state'] = NORMAL
    loading_label['state'] = DISABLED

    display_stats(image)


def compress():
    image_details['text'] = ""
    compressed_image_details['text'] = ""
    compress_ratio_details['text'] = ""
    compressed_image['image'] = ""
    result = ["null"]
    global compressed_image_string
    clear_button['state'] = DISABLED
    compress_button['state'] = DISABLED
    upload_image_button['state'] = DISABLED
    loading_label['state'] = NORMAL
    compressed_image['image'] = ""

    if k_means_Entry.get() != "":
        if k_means_Entry.get().isnumeric() is False or int(k_means_Entry.get()) < 1 or int(k_means_Entry.get()) > 255:
            messagebox.showwarning(title="Error", message="K should be an integer between 1 and 255")
            return
        else:
            compressed_image_string = threading.Thread(target=compressions_k_means.compress,
                                                       args=(image, result, int(k_means_Entry.get())))
    else:
        compressed_image_string = threading.Thread(target=compressions_k_means.compress,
                                                   args=(image, result, None))

    compressed_image_string.start()
    # Wait till the thread is finished running , The main thread is stuck
    # after its returned the name of the saved image as string show it on the screen next to the orig image
    threading.Thread(target=open_compressed_image, args=(result,)).start()


def display_stats(image):
    compressed_image_path = image.filename
    index = 0
    for i in range(0, len(compressed_image_path) - 1):
        if compressed_image_path[i] == '/':
            index = i
    if k_means_Entry.get() == "":
        compressed_image_path = compressed_image_path[0:index] + "compressed_" + "5_colors.png"
    else:
        compressed_image_path = compressed_image_path[0:index] + "compressed_" + str(
            int(k_means_Entry.get())) + "_colors.png"

    image_file_size = os.path.getsize(image.filename)
    image_details['text'] = "image size: " + str(image_file_size) + " bytes"
    compressed_image_file_size = os.path.getsize(compressed_image_path)
    compressed_image_details['text'] = "compressed image size: " + str(compressed_image_file_size) + " bytes"
    compress_ratio = (image_file_size - compressed_image_file_size) / compressed_image_file_size
    compress_ratio_details['text'] = "compress ratio: " + str(compress_ratio * 100) + " %"


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
exit_button = Button(root, text="Exit", command=root.destroy)
progress = tkinter.ttk.Progressbar(root, orient=HORIZONTAL, length=200, mode='indeterminate')
loading_label = Label(root, text="loading...", fg="#2191fb")
k_means_label = Label(root, text="k-means:")
k_means_Entry = Entry(root, bd=5)
stats_label = Label(root, text="Stats:")
canvas_stats = Canvas(root, width=200, height=100, bg="#FFFFFF")
image_details = Label(root, text="", bg="#FFFFFF")
compressed_image_details = Label(root, text="", bg="#FFFFFF" )
compress_ratio_details = Label(root, text="", bg="#FFFFFF")

# Size of the screen
root.geometry("700x700")


image_container.place(x=100, y=100)
compressed_image.place(x=400, y=100)
label.place(relx=0.13)
upload_image_button.place(x=180, y=600)
compress_button.place(x=330, y=600)
clear_button.place(x=430, y=600)
exit_button.place(x=500, y=600)
progress.place(x=250, y=650)
loading_label.place(x=300, y=680)
k_means_label.place(x=240, y=400)
k_means_Entry.place(x=300, y=400)
stats_label.place(x=260, y=450)
canvas_stats.place(x=300, y=450)
image_details.place(x=300, y=450)
compressed_image_details.place(x=300, y=470)
compress_ratio_details.place(x=300, y=490)


# Initiate the main loop
root.mainloop()
