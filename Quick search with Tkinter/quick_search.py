from tkinter import *
from tkinter.font import Font
import webbrowser

root = Tk()
root.title("Quick search!")
root.config(bg="#C7E8CA")
my_font = Font(family="Times new roman", size=15)


def click_google():
    command = search_word_entry.get()
    webbrowser.open("https://www.google.com/search?q=" + command)


def click_filmi():
    command = search_word_entry.get()
    webbrowser.open("https://www.google.com/search?q=" + f"Filmi7 {command}")


def click_youtube():
    command = search_word_entry.get()
    webbrowser.open("https://www.youtube.com/results?search_query=" + command)


def click_linkedin():
    command = search_word_entry.get()
    webbrowser.open("https://www.linkedin.com/search/results/all/?keywords=" + command)


def click_facebook():
    command = search_word_entry.get()
    webbrowser.open("https://www.facebook.com/search/top/?q=" + command)


entry_font = Font(family="Arial Black", size=20)
search_word_entry = Entry(font=entry_font)
search_word_entry.grid(row=1, column=1, columnspan=8)

google_button = Button(text="Google", font=my_font, bg="#62CDFF", command=lambda: click_google())
google_button.grid(row=2, column=1, columnspan=1)

filmi7_button = Button(text="Filmi7", font=my_font, bg="#62CDFF", command=lambda: click_filmi())
filmi7_button.grid(row=2, column=2, columnspan=1)

youtube_button = Button(text="Youtube", font=my_font, bg="#62CDFF", command=lambda: click_youtube())
youtube_button.grid(row=2, column=3, columnspan=1)

linkedin_button = Button(text="LinkedIn", font=my_font, bg="#62CDFF", command=lambda: click_linkedin())
linkedin_button.grid(row=2, column=4, columnspan=1)

facebook_button = Button(text="Facebook", font=my_font, bg="#62CDFF", command=lambda: click_facebook())
facebook_button.grid(row=2, column=5, columnspan=1)

root.mainloop()
