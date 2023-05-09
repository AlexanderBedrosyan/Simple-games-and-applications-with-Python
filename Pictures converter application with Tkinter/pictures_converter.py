from PIL import Image
import PIL.Image
from pillow_heif import register_heif_opener
import os
from tkinter import *
from tkinter import filedialog as fd

root = Tk()
root.geometry("380x380")
root.title("Images converter")
root.resizable(False, False)
icon = PhotoImage(file='convert_imagesplitter.png')
root.iconphoto(False, icon)


def convert_png():
    help(register_heif_opener)
    register_heif_opener()
    filename = fd.askopenfilename()
    current_filename = filename.replace("/", "\\")
    temp_img = PIL.Image.open(current_filename)
    png_photo = current_filename.replace('.HEIC', '.png')
    temp_img.save(png_photo)


def convert_jpg():
    help(register_heif_opener)
    register_heif_opener()
    filename = fd.askopenfilename()
    current_filename = filename.replace("/", "\\")
    temp_img = PIL.Image.open(current_filename)
    jpg_photo = current_filename.replace('.HEIC', '.jpg')
    temp_img.save(jpg_photo)


img = PhotoImage(file="convert_imagesplitter.png")  # import picture
Label(root, image=img, bg="white").place(x=7, y=6)


browse = Label(text="Choose a picture in HEIC", font="Ariel", bd=1, bg="#FFFFE8")
browse.place(x=75, y=5)

myButton = Button(text="Convert to png", font="Ariel, 13", bd=4, command=convert_png)
myButton.place(x=15, y=330)

myButton2 = Button(text="Convert to jpg", font="Ariel, 13", bd=4, command=convert_jpg)
myButton2.place(x=240, y=330)


root.mainloop()
