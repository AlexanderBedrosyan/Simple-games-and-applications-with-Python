from tkinter import *
from tkinter.font import Font
from random import randint

root = Tk()
root.title("Password generator")
root.minsize(520, 200)
root.config(bg="#FFEBB4")
my_font_of_text = Font(
    family="Times",
    size=20
)

first_key_word_list = []
second_key_word_list = []
ascii_numbers = []
ascii_symbols = []


def MyButtonClick():
    global first_key_word_list, second_key_word_list
    first_current = first_key_box.get()
    second_current = second_key_box.get()
    current_list_one = [str(ch) for ch in first_current]
    current_list_two = [str(item) for item in second_current]
    for i in range(0, 3):
        first_key_word_list.append(current_list_one[i])
        second_key_word_list.append(current_list_two[i])

    for i in range(0, 4):
        if i % 2 == 0:
            number = randint(48, 57)
            ascii_numbers.append(chr(number))
        else:
            number = randint(33, 47)
            ascii_symbols.append(chr(number))
    new_password = f"{''.join(first_key_word_list)}{''.join(ascii_symbols)}{''.join(second_key_word_list)}" \
                   f"{''.join(ascii_numbers)}"
    new_password_box.insert(0, new_password)


first_key_word = Label(root, text="First key word", font=my_font_of_text, bg="#FFEBB4")
first_key_word.grid(row=1, column=1, columnspan=1)
first_key_box = Entry(root, width=15, font=my_font_of_text)
first_key_box.grid(row=1, column=2, columnspan=8)


second_key_word = Label(root, text="Second key word", font=my_font_of_text, bg="#FFEBB4")
second_key_word.grid(row=2, column=1, columnspan=1)
second_key_box = Entry(root, width=15, font=my_font_of_text)
second_key_box.grid(row=2, column=2, columnspan=8)


my_font_new_password = Font(
    family="Times",
    size=32
)
myButton = Button(root, width=16, height=1, text="Generate password", font=my_font_of_text,
                   command=lambda: MyButtonClick())
myButton.grid(row=3, column=0, columnspan=6)
new_password_box = Entry(root, width=12, font=my_font_new_password)
new_password_box.grid(row=3, column=8, columnspan=8)

explanation = Label(root, text="The generator will take only",
                    font=my_font_of_text, bg="#FFEBB4")
explanation.grid(row=4, column=1, columnspan=18)
explanation2 = Label(root, text="first 3 letters of each key word!",
                    font=my_font_of_text, bg="#FFEBB4")
explanation2.grid(row=5, column=1, columnspan=18)

root.mainloop()