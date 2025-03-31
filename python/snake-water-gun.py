import random

computer = "Computer"
player = input("Enter your name: ")

n = int(input("Enter the number of rounds to play: "))

computer_point = 0
player_point = 0

def swg(computer_choice, player_choice, computer_point, player_point):
    if computer_choice == player_choice:
        print("It's a draw!")
    elif (computer_choice == "s" and player_choice == "w" or 
          computer_choice == "w" and player_choice == "g" or 
          computer_choice == "g" and player_choice == "s"):
        computer_point += 1
        print(f"{computer} wins this round!")
    elif (player_choice == "s" and computer_choice == "w" or 
          player_choice == "w" and computer_choice == "g" or 
          player_choice == "g" and computer_choice == "s"):
        player_point += 1
        print(f"{player} wins this round!")
    else:
        print(f"Please enter correct value in the input ...... ")
    return computer_point, player_point

def win(computer_point, player_point):
    if computer_point > player_point:
        print(f"\n{computer} has won the game by {computer_point - player_point} points!")
    elif player_point > computer_point:
        print(f"\n{player} has won the game by {player_point - computer_point} points!")
    else:
        print("\nThe game is a draw!")

for i in range(n):
    computer_choice = random.choice(["s", "w", "g"])
    player_choice = input(f"{player}, enter 's' for Snake, 'w' for Water, 'g' for Gun: ").lower()
    print(f"{computer} chose: {computer_choice}")
    computer_point, player_point = swg(computer_choice, player_choice, computer_point, player_point)

win(computer_point, player_point)
