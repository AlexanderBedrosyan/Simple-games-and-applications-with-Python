from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Login app")
root.geometry("925x500+300+200")
root.config(bg="#fff")
root.resizable(False, False) # stop the maximize button on top right corner


def check_the_details():
    username = user.get()
    psswrd = password.get()
    if username == "Dimityr" and psswrd == "Iliev":
        screen = Toplevel(root)
        screen.title("Second page")
        screen.geometry("925x500+300+200")
        screen.config(bg="black")

        Label(screen, text="Welcome to Lokomotiv Plovdiv official page!", fg="white", bg="black",
              font=('Arial Black', 28, "bold")).pack(expand=True)

        screen.mainloop()
    if username != "Dimityr" or psswrd != "Iliev":
        messagebox.showerror("Invalid", "Wrong username or password!")


img = PhotoImage(file="download.png")  # import picture
Label(root, image=img, bg="white").place(x=50, y=50)

img2 = PhotoImage(file="id-profile-user-icon--icon-search-engine-17.png")  # import picture
Label(root, image=img2, bg="white").place(x=470, y=200)

signature = Label(text="Created by Alexander Bedrosyan", fg="black", bg="white", font=('Brush Script MT', 23, "bold"))
signature.place(x=15, y=400)

frame = Frame(root, width=350, height=200, bg="white")
frame.place(x=460, y=50)

heading = Label(frame, text="Sign in", fg="#57a1f8", bg="white", font=('Microsoft YaHei UI Light', 23, "bold"))
heading.place(x=110, y=5)

user = Entry(frame, width=25, fg="black", bg="white", font=('Microsoft YaHei UI Light', 11))
user.place(x=70, y=60)
user.insert(0, "Enter your username")

password = Entry(frame, width=25, fg="black", bg="white", font=('Microsoft YaHei UI Light', 11))
password.place(x=70, y=100)
password.insert(0, "Enter your password")

sign_button = Button(frame, text="Sign in", fg="white", bg="black", font=('Arial Black', 15), command=lambda:
check_the_details())
sign_button.place(x=120, y=140)

root.mainloop()
