from tkinter import *
from forex_python.converter import CurrencyRates
from tkinter.font import Font
import tkinter.messagebox

root = Tk()
root.title("Currency convertor")
root.config(bg="#F3E8FF")
root.minsize(200, 100)
my_font_of_text = Font(family="Ariel", size=15)
currency = CurrencyRates()


def currency_exchange():
    global currency
    from_currency = variable1.get()
    to_currency = variable2.get()
    if from_currency == "CURRENCY" or to_currency == "CURRENCY" or from_currency == to_currency:
        tkinter.messagebox.showinfo("Error!",
                                    "Currency Not Selected or they are equal.\n"
                                    " Please select FROM and TO Currency from the menu.")

    amount = entry_box_from.get()
    current_list = [str(ch) for ch in amount]
    numbers = True
    for i in range(len(current_list)):
        if 0 <= ord(current_list[i]) <= 47 or 58 <= ord(current_list[i]) <= 127:
            numbers = False

    if numbers:
        result = currency.convert(from_currency, to_currency, float(amount))
        entry_box_to.insert(0, result)
    else:
        tkinter.messagebox.showinfo("Error!",
                                    "You must use only numbers!")


CurrenyCode_list = ["USD", "CAD", "CNY", "DKK", "EUR", "BGN", "NOK", "SEK"]

variable1 = StringVar(root)
variable2 = StringVar(root)
variable1.set("CURRENCY")
variable2.set("CURRENCY")
FromCurrency_option = OptionMenu(root, variable1, *CurrenyCode_list)
ToCurrency_option = OptionMenu(root, variable2, *CurrenyCode_list)
FromCurrency_option.config(bg="#DAF5FF")
ToCurrency_option.config(bg="#DAF5FF")
FromCurrency_option.grid(row=1, column=3, ipadx=45, sticky=E)
ToCurrency_option.grid(row=2, column=3, ipadx=45, sticky=E)

from_label = Label(text="From", font=my_font_of_text, bg="#DAF5FF")
from_label.grid(row=1, column=1)
to_label = Label(text="To", font=my_font_of_text)
to_label.grid(row=2, column=1)

entry_box_from = Entry(root, width=15, font=my_font_of_text)
entry_box_from.grid(row=1, column=2)
entry_box_to = Entry(root, width=15, font=my_font_of_text)
entry_box_to.grid(row=2, column=2)

convert_button = Button(root, width=16, height=1, text="Convert", font=my_font_of_text, bg="#DAF5FF",
                   command=lambda: currency_exchange())
convert_button.grid(row=4, column=2, columnspan=2)

root.mainloop()
