import random

op = ("rock","paper","scissors")
running = True 

while True:

    player = None
    computer = random.choice(op)

    while player not in op:
        player = input("Enter a choice (rock,paper,scissors): ")

    print(f"player choice is: {player}")
    print(f"computer choice is: {computer}")
    
    if player == computer:
        print("it is a tie")
    elif player == "rock" and computer == "scissors":
        print ("you win")
    elif player == "paper" and computer == "rock":
        print("you win")
    elif player == "scissors" and computer == "paper":
        print("you win")
    else:
        print( "you lose")

    again = input("play again? (y/n): ").lower()
    if not again == "y":
        running = False
        break;
print("Thanks for playing")

