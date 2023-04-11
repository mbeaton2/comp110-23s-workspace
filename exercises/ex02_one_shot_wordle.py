"""EX02- One Shot Wordle!"""

__author__ = "730480912"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
guess: str = str(input("What is your 6-letter guess? "))
SECRET: str = "python"
result = ""

if len(guess) < int(6) or len(guess) > int(6):
    print("That was not 6 letters! Try again: ")

else:
    for index in range(0, len(guess)):
        if guess[index] == SECRET[index]:
            result = result + GREEN_BOX
            print("Woo! You got it! ")
        else:  
            search = False
            for otherindex in range(0, len(SECRET)):
                if index != otherindex and guess[index] == SECRET[otherindex]:
                    search = True

            if search == True:
                result = result + YELLOW_BOX 
            else:
                result = result + WHITE_BOX 
                print("Not quite. Play again soon!")
             
    print(result)