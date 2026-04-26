import random

def sps():
    name = input("Enter your name: ")

    user_score = 0
    computer_score = 0

    options = ["stone", "paper", "scissors"]

    while True:
        print("\n1. Play")
        print("2. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            user = input("Enter stone/paper/scissors: ").lower()
            computer = random.choice(options)

            print(name, "chose:", user)
            print("Computer chose:", computer)

            if user == computer:
                print("Draw")
            elif (user == "stone" and computer == "scissors") or \
                 (user == "paper" and computer == "stone") or \
                 (user == "scissors" and computer == "paper"):
                print(name, "wins this round")
                user_score += 1
            else:
                print("Computer wins this round")
                computer_score += 1

            print("Score ->", name + ":", user_score, " Computer:", computer_score)

        elif choice == "2":
            print("\nFinal Score ->", name + ":", user_score, " Computer:", computer_score)

            if user_score > computer_score:
                print(name, "is the winner")
            elif user_score < computer_score:
                print("Computer is the winner")
            else:
                print("Match Draw")

            break
        else:
            print("Wrong choice")