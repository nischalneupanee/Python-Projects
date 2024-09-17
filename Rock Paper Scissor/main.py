import random as r

user_wins = 0
computer_wins = 0

options = ["rock", "paper","scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit").lower()
    if user_input == 'q':
        break

    if user_input not in options:
        continue

    random_numer = r.randint(0,2)
    # rock : 0, paper: 1, scissor :2
    computer_pick = options[random_numer]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins +=1
        continue

    elif user_input == "scissor" and computer_pick == "paper":
        print("You won!")
        user_wins += 1
        continue

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1
        continue

    else:
        print("You lost")
        computer_wins +=1


print("You win", user_wins, "times." )
print("Computer win", computer_wins, "times." )
print("Goodbye")