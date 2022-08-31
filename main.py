# Rock Scissors and Paper game
import random

print(f"Welcome to the Game 🥳\nWhat do you Choose?")
def game():
    playcount = 1
    Computerwinrate = 0
    Userwinrate = 0
    while playcount <= 3:
        userChose = int(input('Type 0 for Rock, 1 for Paper or 2 For Scissors : '))
    #Making the list and taking out Random values from it
    # 0 -->Rock
    # 1 -->Paper
    # 3 -->Scissors
        list_game = ["Rock","Paper","Scissors"]
        randomChoice = random.choice(list_game)
        print("\nComputer Choice\n ",randomChoice)

        user = list_game[userChose]

        if user == "Rock" or "Paper" or "Scissors":
            if randomChoice == user:
                print("Draw")

            if randomChoice == "Rock":
                if user == "Paper":
                    print("You Win")
                    Userwinrate += 1

                else:
                    print("You Loose")
                    Computerwinrate += 1

            elif randomChoice == "Paper":
                if user == "Rock":
                    print("You win the match")
                    Userwinrate += 1

                else:
                    print("You loose")
                    Computerwinrate += 1

            elif randomChoice == "Scissors":
                if user == "Paper":
                    print("You loose")
                    Computerwinrate += 1

                else:
                    print("You Win")
                    Userwinrate += 1

            else:
                print("Enter Valid number")
        playcount += 1
    return Userwinrate, Computerwinrate

Userwinrate, Computerwinrate = game()
if Userwinrate > Computerwinrate:
    print("You Are the Winner of this Game")
elif Userwinrate == Computerwinrate:
    print("This game is draw")
    game()
else:
    print("Computer Win this Match")





