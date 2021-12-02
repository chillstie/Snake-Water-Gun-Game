from random import choice 

user = input("\nEnter Your Name : ")
name = user.capitalize()

def scorewrite():
    """This function write the score in txt file"""
    data = f"\nRound {rounds} - {winner}"
    with open("Score.txt","a") as score:
        score.write(data)
    
def scoreread():
    """This fuction read the txt file score after game ends"""
    with open("Score.txt") as file:
        score = file.read()
    return score

def scoreupdate():
    """This fuction update txt file into blank delete old score and set blank, this one is recommended"""
    with open("Score.txt","w") as score:
        update = score.write("*** Scoreboard ***")

scoreupdate()

comp = 0
plyr = 0
rounds = 0

while rounds < 10:
    options = ["Snake", "Water", "Gun"]
    computer = choice(options)

    print ("\nRound",rounds + 1)

    print ("\nFor Snake Press [S]")
    print ("For Water Press [W]")
    print ("For Gun Press [G]")

    player = input("\nEnter Your Key : ").capitalize()

    if player == "S":
        if computer == "Snake":
            winner = "Darw"
            rounds += 1
            print ("\n-- Draw --")
            print (f"Computer Have {comp} Points - {name} Have {plyr} Points")
            scorewrite()

        elif computer == "Water":
            winner = name
            plyr += 1
            rounds += 1
            print ("\n-- Won -- ")
            print (f"Computer Have {comp} Points - {name} Have {plyr} Points")   
            scorewrite()
        else:
            winner = "Computer"
            comp += 1
            rounds += 1
            print ("\n-- Lose --")
            print (f"Computer Have {comp} Points - {name} Have {plyr} Points")
            scorewrite()

    elif player == "W":
        if computer == "Water":
            winner = "Draw"
            rounds += 1
            print ("\n-- Darw --")
            print (f"Computer Have {comp} Points - {name} Have {plyr} Points")
            scorewrite()

        elif computer == "Snake":
            winner = "Computer"
            comp += 1
            rounds += 1
            print ("\n-- Lost --")
            print (f"Computer Have {comp} Points - {name} Have {plyr} Points")
            scorewrite()
        else:
            winner = name
            plyr += 1
            rounds += 1
            print ("\n-- Won --")
            print (f"Computer Have {comp} Points - {name} Have {plyr} Points")
            scorewrite()

    elif player == "G":
        if computer == "Gun":
            winner = "Draw"
            rounds += 1
            print ("\n-- Darw --")
            print (f"Computer Have {comp} Points - {name} Have {plyr} Points")
            scorewrite()

        elif computer == "Water":
            winner = "Computer"
            comp += 1
            rounds += 1
            print ("\n-- Lost --")
            print (f"Computer Have {comp} Points - {name} Have {plyr} Points")
            scorewrite()
        else:
            winner = name
            plyr += 1
            rounds += 1
            print ("\n-- Won --")
            print (f"Computer Have {comp} Points - {name} Have {plyr} Points")
            scorewrite()
    else:
        print ("\nWrong Key...")

if comp == plyr:
    print ("\nResults")
    print (scoreread())
    print ("\n--- The Game is Draw ---\n")

elif comp > plyr:
    print ("\nResults")
    print (scoreread())
    print ("\n*** You Lose The Game ***\n")

else:
    print ("\nResults")
    print (scoreread())
    print ("\n*** You Won The Game ***\n")