from tkinter import *
from tkinter import Label
import webbrowser

root = Tk()
root.title("Lyrics app")
root.iconbitmap("D:/PyCharmProjects/PycharmProjects/tkinter_3/musical note.ico") # have to convert every picture in ICO
root.geometry("910x700")
root.resizable(False, False)


def text():
    autor_name = autor_box.get()
    song_name = song_box.get()
    if " " in autor_name:
        autor_name = autor_name.replace(" ", "-")
    if " " in song_name:
        song_name = song_name.replace(" ", "-")

    webbrowser.open("https://textove.com/" + autor_name + "-" + song_name + "-tekst")


img = PhotoImage(file="D:/PyCharmProjects/PycharmProjects/tkinter_3/piano.png")
Label(root, image=img, bg="white").place(x=0, y=0)

autor_box = Entry(width=25, fg="black", bg="white", font=('Calibri', 11))
autor_box.place(x=200, y=200)
autor_box.insert(0, "Autor")

song_box = Entry(width=25, fg="black", bg="white", font=('Calibri', 11))
song_box.place(x=200, y=240)
song_box.insert(0, "Song name")

sign_button = Button(root, text="Generate text", fg="white", bg="grey", font=('Calibri', 15), command=lambda:
text())
sign_button.place(x=200, y=280)


root.mainloop()
