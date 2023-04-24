from tkinter import *
import qrcode

root = Tk()
root.title("QR generator")
root.geometry("1000x500")
root.config(bg="#BDCDD6")
root.resizable(False, False)


def generate():
    name = title.get()
    needed_link = link.get()
    qr = qrcode.make(needed_link)
    qr.save("Qrcodes/" + str(name) + ".png")

    global Image
    Image = PhotoImage(file="Qrcodes/" + str(name) + ".png")
    Image_view.config(image=Image)


Image_view=Label(root, bg="#BDCDD6")
Image_view.pack(padx=50, pady=10, side=RIGHT)

Label(root, text="Title", fg="Black", bg="#BDCDD6", font=15).place(x=50, y=150)
title = Entry(root, font=16)
title.place(x=53, y=180)

Label(root, text="Import link", bg="#BDCDD6", font=15).place(x=50, y=220)
link = Entry(root, font=16)
link.place(x=53, y=250)

Button(root, text="Generate", width=20, height=2, bg="black", fg="white", command=generate).place(x=53, y=300)

root.mainloop()
