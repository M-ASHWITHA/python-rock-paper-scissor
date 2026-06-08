import random

while True:
    play=input("Let's start the game? (y/n): ").lower()
    if play=="n":
        print("Okay, bye!")
        quit()
    elif play=="y":
        print("Welcome to the game!")
        break
    else:
        print("Please enter a valid input.")
        continue

options=["rock", "paper", "scissor"]
win=0
lose=0
matches=0
while True:
    random_number=random.randint(0,2)
    computer_pick=options[random_number]

    user_pick=input("rock paper or scissor?: ").lower()
    if user_pick not in options:
        print("Please enter rock or paper or scissor")
        continue

    print(f"You have chosen: {user_pick}")
    print(f"Computer have chosen: {computer_pick}")
    matches+=1

    if (user_pick=="rock" and computer_pick=="scissor" or 
        user_pick=="paper" and computer_pick=="rock" or 
        user_pick=="scissor" and computer_pick=="paper"):
        print("You win!")
        win+=1

    elif user_pick==computer_pick:
        print("Tie!")
    else:
        print("You lose.")
        lose+=1

    again=input("Play again? (y/n): ").lower()
    if again=="n":
        print("Happy playing with you! Bye.")
        if win>lose:
            print("You won!! :)")
        elif win<lose:
            print("You lost :(")
        else:
            print("Tie :o")
        print(f"Your score: {win}/{matches}")
        break
    elif again=="y":
        continue
    else:
        print("Enter y or n.")
        continue
