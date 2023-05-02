from tkinter import *
from random import randint

root = Tk()
root.title("Rock Paper Scissors.app")
root.iconbitmap("D:/PyCharmProjects/PycharmProjects/tkinter_3/rock-paper-scissors.ico")
root.geometry("700x300")
root.resizable(False, False)

rock_paper_scissors_list = ["rock", "paper", "scissors"]
player_option = None
draw_img = PhotoImage(file="no winner.png")
winner_img = PhotoImage(file="winner.png")
lost_img = PhotoImage(file="game over.png")


def result(number):
    player_option = rock_paper_scissors_list[int(number)]
    computer_choice = rock_paper_scissors_list[int(randint(0, 2))]
    if computer_choice == player_option:
        screen = Toplevel(root)
        screen.title("Result page")
        screen.geometry("1000x800")
        screen.config(bg="black")
        screen.resizable(False, False)

        Label(screen, image=draw_img, fg="white", bg="black",
              font=('Arial Black', 28, "bold")).pack(expand=True)
        Label(screen, text=f"Тhe computer selected {computer_choice}.\n No one wins!",fg="white", bg="black",
              font=('Arial Black', 28, "bold")).place(x=180, y=2)
    else:
        if (computer_choice == rock_paper_scissors_list[0] and player_option == rock_paper_scissors_list[1]) \
                or (computer_choice == rock_paper_scissors_list[1] and player_option == rock_paper_scissors_list[2]) \
                or (computer_choice == rock_paper_scissors_list[2] and player_option == rock_paper_scissors_list[0]):
            screen = Toplevel(root)
            screen.title("Result page")
            screen.geometry("1000x800")
            screen.config(bg="black")
            screen.resizable(False, False)

            Label(screen, image=winner_img, fg="white", bg="black",
                  font=('Arial Black', 28, "bold")).pack(expand=True)
            Label(screen, text=f"Тhe computer selected {computer_choice}.\n You are the winner!", fg="white", bg="black",
                  font=('Arial Black', 28, "bold")).place(x=190, y=1)
        elif (computer_choice == rock_paper_scissors_list[0] and player_option == rock_paper_scissors_list[2])\
                or (computer_choice == rock_paper_scissors_list[1] and player_option == rock_paper_scissors_list[0]) \
                or (computer_choice == rock_paper_scissors_list[2] and player_option == rock_paper_scissors_list[0])\
                or (computer_choice == rock_paper_scissors_list[2] and player_option == rock_paper_scissors_list[1]):
            screen = Toplevel(root)
            screen.title("Result page")
            screen.geometry("1000x800")
            screen.config(bg="black")
            screen.resizable(False, False)

            Label(screen, image=lost_img, fg="white", bg="black",
                  font=('Arial Black', 28, "bold")).pack(expand=True)
            Label(screen, text=f"Тhe computer selected {computer_choice}.\n You lost!", fg="white",
                  bg="black",
                  font=('Arial Black', 28, "bold")).place(x=190, y=1)


img_rock = PhotoImage(file="rock.png")
Label(root, image=img_rock, bg="white").place(x=40, y=40)
rock_button = Button(root, text="Rock", fg="white", bg="grey", font=('Calibri', 30), command=lambda: result(0))
rock_button.place(x=63, y=200)

img_paper = PhotoImage(file="paper.png")
Label(root, image=img_paper, bg="white", fg="white").place(x=260, y=40)
paper_button = Button(root, text="Paper", fg="white", bg="grey", font=('Calibri', 30), command=lambda: result(1))
paper_button.place(x=270, y=200)

img_scissors = PhotoImage(file="scissors.png")
Label(root, image=img_scissors, bg="white", fg="white").place(x=500, y=40)
scissors_button = Button(root, text="Scissors", fg="white", bg="grey", font=('Calibri', 30), command=lambda: result(2))
scissors_button.place(x=500, y=200)

root.mainloop()