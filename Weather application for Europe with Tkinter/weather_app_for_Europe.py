from tkinter import *
from tkinter import Label
import tkinter.messagebox
import requests
from bs4 import BeautifulSoup

root = Tk()
root.title("Weather application")
root.geometry("925x500+300+200")
root.config(bg="#fff")
root.resizable(False, False) # stop the maximize button on top right corner


def checking_weather():
    country_add = country.get()
    city_add = city.get()

    final_link = "https://www.foreca.bg/" + country_add + "/" + city_add + "/" + city_add

    if country_add == "United Kingdom":
        final_link = "https://www.foreca.bg/" + "United-Kingdom/England" + "/" + city_add

    if city_add == "Sofia":
        final_link = "https://www.foreca.bg/" + "Bulgaria/Sofia--Capital/Sofia"

    page = requests.get(final_link)
    soup = BeautifulSoup(page.content, 'html.parser')
    products = soup.select('div.current') # Extract and store in top_items according to instructions on the left if I want to check print(products)
    review_label = ""
    for elem in products:
        review_label = elem.select('span', class_="value temp temp_c")[0].text

    tkinter.messagebox.showinfo("Temperature!", f"The temperature in {city_add} is {review_label}")


frame = Frame(root, width=350, height=200, bg="white")
frame.place(x=250, y=150)

country_label = Label(frame, text="Country", fg="black", bg="white", font=('Microsoft YaHei UI Light', 14))
country_label.place(x=80, y=0)
country = Entry(frame, width=25, fg="black", bg="white", font=('Microsoft YaHei UI Light', 11))
country.place(x=80, y=30)

city_label = Label(frame, text="City", fg="black", bg="white", font=('Microsoft YaHei UI Light', 14))
city_label.place(x=80, y=70)
city = Entry(frame, width=25, fg="black", bg="white", font=('Microsoft YaHei UI Light', 11))
city.place(x=80, y=100)

sign_button = Button(frame, text="Check the temperature", fg="white", bg="black", font=('Arial Black', 15), command=lambda:
checking_weather())
sign_button.place(x=50, y=140)

root.mainloop()
