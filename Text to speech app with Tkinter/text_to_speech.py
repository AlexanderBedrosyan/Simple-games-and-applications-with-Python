from tkinter import *
import pyttsx3

root = Tk()
root.title("Text to speech.app")
root.iconbitmap("D:/PyCharmProjects/PycharmProjects/tkinter_3/sound.ico")
root.geometry("676x400")
root.resizable(False, False)

engine = pyttsx3.init()


def speak():
    engine.say(text.get())
    engine.runAndWait()
    engine.stop()


frame = LabelFrame(root, text="Text to speech", font=20, bd=1)
frame.pack(fill="both", expand="yes", padx=10, pady=10)

img = PhotoImage(file="D:/PyCharmProjects/PycharmProjects/tkinter_3/background.png")
Label(frame, image=img, bg="white").place(x=0, y=0)

Label = Label(frame, text="Type text", font=12, bd=1)
Label.place(x=255, y=70)

text = Entry(frame, font=12)
text.place(x=190, y=30)

btn = Button(frame, text="Speak", font=12, bd=1, command=speak)
btn.place(x=262, y=230)

root.mainloop()