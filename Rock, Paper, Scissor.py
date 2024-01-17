import random
Options=("rock","paper","scissor")
running=True
while running:
    player=None
    computer=random.choice(Options)

    while player not in Options:
        player=input("Enter the choice(rock,paper,scissor):\n")
    print(f"Player:{player}")
    print(f"Computer:{computer}")

    if player==computer:
        print("It's a tie!")

    elif player=="rock" and computer=="scissor":
        print("You Win!")

    elif player=="paper" and computer=="rock":
        print("You Win!")

    elif player=="scissor" and computer=="paper":
        print("YOu Win!")

    else:
        print("You Lose!")

    if not input("Play Again?{Y/N):\n").lower=="y":
        running=False
    print("Thank You")
    