from tkinter import *
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

list_one = []
list_two = []
mov = 0


def CheckWinner():
    if (1 in list_one) and (4 in list_one) and (7 in list_one):
        messagebox.showinfo(title="Congratulations.",
                            message="Player 1 is the winner")
    elif (2 in list_one) and (5 in list_one) and (8 in list_one):
        messagebox.showinfo(title="Congratulations.",
                            message="Player 1 is the winner")
    elif (3 in list_one) and (6 in list_one) and (9 in list_one):
        messagebox.showinfo(title="Congratulations.",
                            message="Player 1 is the winner")
    elif (1 in list_one) and (5 in list_one) and (9 in list_one):
        messagebox.showinfo(title="Congratulations.",
                            message="Player 1 is the winner")
    elif (3 in list_one) and (5 in list_one) and (7 in list_one):
        messagebox.showinfo(title="Congratulations.",
                            message="Player 1 is the winner")
    elif (1 in list_one) and (2 in list_one) and (3 in list_one):
        messagebox.showinfo(title="Congratulations.",
                            message="Player 1 is the winner")
    elif (4 in list_one) and (5 in list_one) and (6 in list_one):
        messagebox.showinfo(title="Congratulations.",
                            message="Player 1 is the winner")
    elif (7 in list_one) and (8 in list_one) and (9 in list_one):
        messagebox.showinfo(title="Congratulations.",
                            message="Player 1 is the winner")

    if (11 in list_two) and (14 in list_two) and (17 in list_two):
        messagebox.showinfo(title="Congratulations.",
                            message="Player 2 is the winner")
    elif (12 in list_two) and (15 in list_two) and (18 in list_two):
        messagebox.showinfo(title="Congratulations.",
                            message="Player 2 is the winner")
    elif (13 in list_two) and (16 in list_two) and (19 in list_two):
        messagebox.showinfo(title="Congratulations.",
                            message="Player 2 is the winner")
    elif (11 in list_two) and (15 in list_two) and (19 in list_two):
        messagebox.showinfo(title="Congratulations.",
                            message="Player 2 is the winner")
    elif (13 in list_two) and (15 in list_two) and (17 in list_two):
        messagebox.showinfo(title="Congratulations.",
                            message="Player 2 is the winner")
    elif (11 in list_two) and (12 in list_two) and (13 in list_two):
        messagebox.showinfo(title="Congratulations.",
                            message="Player 2 is the winner")
    elif (14 in list_two) and (15 in list_two) and (16 in list_two):
        messagebox.showinfo(title="Congratulations.",
                            message="Player 2 is the winner")
    elif (17 in list_two) and (18 in list_two) and (19 in list_two):
        messagebox.showinfo(title="Congratulations.",
                            message="Player 2 is the winner")

    if (len(list_one) + len(list_two)) == 9:
        messagebox.showinfo(title="Draw",
                            message="There is no winner")


def button_for_number(number):
    global list_one, list_two
    current = box1.get()
    box1.delete(0, END)
    box1.insert(0, str(current) + str(number))
    myButton11["state"] = "disabled"
    myButton1["state"] = "disabled"
    list_one.append(1)
    CheckWinner()


def button_for_number11(number):
    global list_one, list_two
    current = box1.get()
    box1.delete(0, END)
    box1.insert(0, str(current) + str(number))
    myButton11["state"] = "disabled"
    myButton1["state"] = "disabled"
    list_two.append(11)
    CheckWinner()


def button_for_number2(number):
    global list_one, list_two
    current = box2.get()
    box2.delete(0, END)
    box2.insert(0, str(current) + str(number))
    myButton12["state"] = "disabled"
    myButton2["state"] = "disabled"
    list_one.append(2)
    CheckWinner()


def button_for_number12(number):
    global list_one, list_two
    current = box2.get()
    box2.delete(0, END)
    box2.insert(0, str(current) + str(number))
    myButton12["state"] = "disabled"
    myButton2["state"] = "disabled"
    list_two.append(12)
    CheckWinner()


def button_for_number3(number):
    global list_one, list_two
    current = box3.get()
    box3.delete(0, END)
    box3.insert(0, str(current) + str(number))
    myButton13["state"] = "disabled"
    myButton3["state"] = "disabled"
    list_one.append(3)
    CheckWinner()


def button_for_number13(number):
    global list_one, list_two
    current = box3.get()
    box3.delete(0, END)
    box3.insert(0, str(current) + str(number))
    myButton13["state"] = "disabled"
    myButton3["state"] = "disabled"
    list_two.append(13)
    CheckWinner()


def button_for_number4(number):
    global list_one, list_two
    current = box4.get()
    box4.delete(0, END)
    box4.insert(0, str(current) + str(number))
    myButton14["state"] = "disabled"
    myButton4["state"] = "disabled"
    list_one.append(4)
    CheckWinner()


def button_for_number14(number):
    global list_one, list_two
    current = box4.get()
    box4.delete(0, END)
    box4.insert(0, str(current) + str(number))
    myButton14["state"] = "disabled"
    myButton4["state"] = "disabled"
    list_two.append(14)
    CheckWinner()


def button_for_number5(number):
    global list_one, list_two
    current = box5.get()
    box5.delete(0, END)
    box5.insert(0, str(current) + str(number))
    myButton5["state"] = "disabled"
    myButton15["state"] = "disabled"
    list_one.append(5)
    CheckWinner()


def button_for_number15(number):
    global list_one, list_two
    current = box5.get()
    box5.delete(0, END)
    box5.insert(0, str(current) + str(number))
    myButton5["state"] = "disabled"
    myButton15["state"] = "disabled"
    list_two.append(15)
    CheckWinner()


def button_for_number6(number):
    global list_one, list_two
    current = box6.get()
    box6.delete(0, END)
    box6.insert(0, str(current) + str(number))
    myButton16["state"] = "disabled"
    myButton6["state"] = "disabled"
    list_one.append(6)
    CheckWinner()


def button_for_number16(number):
    global list_one, list_two
    current = box6.get()
    box6.delete(0, END)
    box6.insert(0, str(current) + str(number))
    myButton16["state"] = "disabled"
    myButton6["state"] = "disabled"
    list_two.append(16)
    CheckWinner()


def button_for_number7(number):
    global list_one, list_two
    current = box7.get()
    box7.delete(0, END)
    box7.insert(0, str(current) + str(number))
    myButton17["state"] = "disabled"
    myButton7["state"] = "disabled"
    list_one.append(7)
    print(list_one)
    CheckWinner()


def button_for_number17(number):
    global list_one, list_two
    current = box7.get()
    box7.delete(0, END)
    box7.insert(0, str(current) + str(number))
    myButton17["state"] = "disabled"
    myButton7["state"] = "disabled"
    list_two.append(17)
    CheckWinner()


def button_for_number8(number):
    global list_one, list_two
    current = box8.get()
    box8.delete(0, END)
    box8.insert(0, str(current) + str(number))
    myButton18["state"] = "disabled"
    myButton8["state"] = "disabled"
    list_one.append(8)
    CheckWinner()


def button_for_number18(number):
    global list_one, list_two
    current = box8.get()
    box8.delete(0, END)
    box8.insert(0, str(current) + str(number))
    myButton18["state"] = "disabled"
    myButton8["state"] = "disabled"
    list_two.append(18)
    CheckWinner()


def button_for_number9(number):
    global list_one, list_two
    current = box9.get()
    box9.delete(0, END)
    box9.insert(0, str(current) + str(number))
    myButton19["state"] = "disabled"
    myButton9["state"] = "disabled"
    list_one.append(9)
    CheckWinner()


def button_for_number19(number):
    global list_one, list_two
    current = box9.get()
    box9.delete(0, END)
    box9.insert(0, str(current) + str(number))
    myButton19["state"] = "disabled"
    myButton9["state"] = "disabled"
    list_two.append(19)
    CheckWinner()


box1 = Entry(root, width=3, font=('Helvetica', 20))
box1.grid(row=0, column=0, columnspan=1)
box2 = Entry(root, width=3, font=('Helvetica', 20))
box2.grid(row=1, column=0, columnspan=1)
box3 = Entry(root, width=3, font=('Helvetica', 20))
box3.grid(row=2, column=0, columnspan=1)

box4 = Entry(root, width=3, font=('Helvetica', 20))
box4.grid(row=0, column=1, columnspan=2)
box5 = Entry(root, width=3, font=('Helvetica', 20))
box5.grid(row=1, column=1, columnspan=2)
box6 = Entry(root, width=3, font=('Helvetica', 20))
box6.grid(row=2, column=1, columnspan=2)

box7 = Entry(root, width=3, font=('Helvetica', 20))
box7.grid(row=0, column=3, columnspan=3)
box8 = Entry(root, width=3, font=('Helvetica', 20))
box8.grid(row=1, column=3, columnspan=3)
box9 = Entry(root, width=3, font=('Helvetica', 20))
box9.grid(row=2, column=3, columnspan=3)


player_one_label = Label(root, text="Player1").grid(row=4, column=7)


myButton1 = Button(root, width=4, height=2, text="1", command=lambda: button_for_number("X"))
myButton1.grid(row=0, column=6, columnspan=4)
myButton2 = Button(root, width=4, height=2, text="4", command=lambda: button_for_number2("X"))
myButton2.grid(row=1, column=6, columnspan=5)
myButton3 = Button(root, width=4, height=2, text="7", command=lambda: button_for_number3("X"))
myButton3.grid(row=2, column=6, columnspan=5)
myButton4 = Button(root, width=4, height=2, text="2", command=lambda: button_for_number4("X"))
myButton4.grid(row=0, column=11, columnspan=5)
myButton5 = Button(root, width=4, height=2, text="5", command=lambda: button_for_number5("X"))
myButton5.grid(row=1, column=11, columnspan=5)
myButton6 = Button(root, width=4, height=2, text="8", command=lambda: button_for_number6("X"))
myButton6.grid(row=2, column=11, columnspan=5)
myButton7 = Button(root, width=4, height=2, text="3", command=lambda: button_for_number7("X"))
myButton7.grid(row=0, column=17, columnspan=6)
myButton8 = Button(root, width=4, height=2, text="6", command=lambda: button_for_number8("X"))
myButton8.grid(row=1, column=17, columnspan=6)
myButton9 = Button(root, width=4, height=2, text="9", command=lambda: button_for_number9("X"))
myButton9.grid(row=2, column=17, columnspan=6)


player_two_label = Label(root, text="Player2").grid(row=9)


myButton11 = Button(root, width=4, height=2, text="1", command=lambda: button_for_number11("O"))
myButton11.grid(row=6, column=0, columnspan=1)
myButton12 = Button(root, width=4, height=2, text="4", command=lambda: button_for_number12("O"))
myButton12.grid(row=7, column=0, columnspan=1)
myButton13 = Button(root, width=4, height=2, text="7", command=lambda: button_for_number13("O"))
myButton13.grid(row=8, column=0, columnspan=1)
myButton14 = Button(root, width=4, height=2, text="2", command=lambda: button_for_number14("O"))
myButton14.grid(row=6, column=1, columnspan=2)
myButton15 = Button(root, width=4, height=2, text="5", command=lambda: button_for_number15("O"))
myButton15.grid(row=7, column=1, columnspan=2)
myButton16 = Button(root, width=4, height=2, text="8", command=lambda: button_for_number16("O"))
myButton16.grid(row=8, column=1, columnspan=2)
myButton17 = Button(root, width=4, height=2, text="3", command=lambda: button_for_number17("O"))
myButton17.grid(row=6, column=3, columnspan=3)
myButton18 = Button(root, width=4, height=2, text="6", command=lambda: button_for_number18("O"))
myButton18.grid(row=7, column=3, columnspan=3)
myButton19 = Button(root, width=4, height=2, text="9", command=lambda: button_for_number19("O"))
myButton19.grid(row=8, column=3, columnspan=3)



root.mainloop()
