from tkinter import *

root = Tk()
root.title("Noob Calculator :D")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=20, pady=20)
# box place - (row and column - always starting from zero), columnspan - number of boxes, padx/pady - cordinate system

def button_for_number(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

# Function - button for the insert numbers of the bellow buttons, e.insert - concatenate next number

def button_delete():
    e.delete(0, END)
# Define the function to delete everything in the entry box, then we dont need lambda,
# just command=button_delete on the below

def button_plus():
    first_number = e.get() # getting the first using number
    global f_num # common function for saving the process and finishing with equal
    global total # adding in next global file, this will help for if statements and correcting the final results
    total = "plus"
    f_num = int(first_number) # converting to int
    e.delete(0, END) # clearing the text box

def button_minus():
    first_number = e.get()  # getting the first using number
    global f_num  # common function for saving the process and finishing with equal
    global total  # adding in next global file
    total = "minus"
    f_num = int(first_number)  # converting to int
    e.delete(0, END)

def button_division():
    first_number = e.get() # getting the first using number
    global f_num # common function for saving the process and finishing with equal
    global total # adding in next global file
    total = "div"
    f_num = int(first_number) # converting to int
    e.delete(0, END)

def button_multiplication():
    first_number = e.get()  # getting the first using number
    global f_num  # common function for saving the process and finishing with equal
    global total  # adding in next global file
    total = "multip"
    f_num = int(first_number)  # converting to int
    e.delete(0, END)

def button_equal():
    second_number = e.get() # same as button_plus, this time is not needed to use global
    e.delete(0, END)
    if total == "plus":
        e.insert(0, f_num + int(second_number)) # using the f_numb(global) then add the new number
    elif total == "minus":
        e.insert(0, f_num - int(second_number))
    elif total == "div":
        e.insert(0, f_num / int(second_number))
    elif total == "multip":
        e.insert(0, f_num * int(second_number))


one = Button(root, text="1", padx=40, pady=20, command=lambda: button_for_number(1))
two = Button(root, text="2", padx=40, pady=20, command=lambda: button_for_number(2))
three = Button(root, text="3", padx=40, pady=20, command=lambda: button_for_number(3))
four = Button(root, text="4", padx=40, pady=20, command=lambda: button_for_number(4))
five = Button(root, text="5", padx=40, pady=20, command=lambda: button_for_number(5))
six = Button(root, text="6", padx=40, pady=20, command=lambda: button_for_number(6))
seven = Button(root, text="7", padx=40, pady=20, command=lambda: button_for_number(7))
eight = Button(root, text="8", padx=40, pady=20, command=lambda: button_for_number(8))
nine = Button(root, text="9", padx=40, pady=20, command=lambda: button_for_number(9))
zero = Button(root, text="0", padx=40, pady=20, command=lambda: button_for_number(0))

# text(box), padx/pady(cordinate system), lambda add the number onto the entry box (button for number)

plus = Button(root, text="+", padx=39, pady=20, command=button_plus)
minus = Button(root, text="-", padx=40.4, pady=20, command=button_minus)
division = Button(root, text="/", padx=40.5, pady=20, command=button_division)
multiplication = Button(root, text="*", padx=40, pady=20, command=button_multiplication)
delete = Button(root, text="Delete", padx=27, pady=20, command=button_delete)
equal = Button(root, text="=", padx=39, pady=20, command=button_equal)
for_fun = Button(root,text="Само", padx=30, pady=20, command=lambda: button_for_number("Само"))
for_fun2 = Button(root,text="Локо", padx=30, pady=20, command=lambda: button_for_number(" Локо"))

# grid defines correct place - it looks like square with small squares inside

one.grid(row=3, column=0)
two.grid(row=3, column=1)
three.grid(row=3, column=2)

four.grid(row=2, column=0)
five.grid(row=2, column=1)
six.grid(row=2, column=2)

seven.grid(row=1, column=0)
eight.grid(row=1, column=1)
nine.grid(row=1, column=2)

plus.grid(row=4, column=0)
zero.grid(row=4, column=1)
minus.grid(row=4, column=2)

division.grid(row=5, column=0)
delete.grid(row=5, column=1, columnspan=1)
multiplication.grid(row=5, column=2)

for_fun.grid(row=6, column=0)
equal.grid(row=6, column=1)
for_fun2.grid(row=6, column=2)

root.mainloop()
