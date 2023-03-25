from random import randint


def selected_options(number):
    game_task = int(number) - 1
    return game_task


game_list = ["1", "2", "3"]
rock_paper_scissors_list = ["rock", "paper", "scissors"]
final_list = []

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
final_list.append(rock)
paper = '''
    ______
---'   ___)_____
          ______)
          _______)
         _______)
---.__________)
'''
final_list.append(paper)
scissors = '''
    ______
---'   ___)_____
          ______)
       __________)
      (___)
---.__(__)
'''
final_list.append(scissors)
player_option = 0
computer_choice = randint(1, 3)

while True:
    option = input("1.Rock\n2.Paper\n3.Scissors\nSelect an option: ")
    if option in game_list:
        player_option = int(option)
        print(f"My choice is: {rock_paper_scissors_list[selected_options(option)]}")
        print(*final_list[selected_options(option)])
        break
    else:
        print("INVALID OPTION. You have to choose from the numbers - 1, 2, 3!")

print("VS.")
print(f"Computer's choice is: {rock_paper_scissors_list[selected_options(computer_choice)]}")
print(*final_list[selected_options(computer_choice)])

if computer_choice == player_option:
    print("We ended the game in a draw!")
else:
    if (computer_choice == 1 and player_option == 2) or (computer_choice == 2 and player_option == 3) \
            or (computer_choice == 3 and player_option == 1):
        print("You win!")
    elif (computer_choice == 1 and player_option == 3) or (computer_choice == 2 and player_option == 1) \
            or (computer_choice == 3 and player_option == 1) or (computer_choice == 3 and player_option == 2):
        print("You lost!")
