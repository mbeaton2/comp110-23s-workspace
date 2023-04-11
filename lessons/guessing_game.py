"""Asks user for a number, goes until they get it right"""

SECRET: int = 4
guess: int = int(input("Guess a number! "))
playing: bool = True
number_of_guesses: int = 1
while playing and number_of_guesses < 6:
    print("Number of guesses " + str(number_of_guesses))
    
    if guess == SECRET: 
        print("Yay! You got it right! ")
        playing = False
    else:
        print("Wrong number :( ")
        if guess % 2 == 1: #guess is odd
            print("Your guess is odd. The answer is even! ")
        if guess > SECRET:
            print("Your guess is too high! ")
        else: #guess < SECRET
             print("Your guess is too low! ")
        guess = int(input("Make another guess! "))
    number_of_guesses = number_of_guesses + 1
    print("NUmber of guesses " + str(number_of_guesses))

if guess == SECRET[1]:
        print(GREEN_BOX[1])
    else:
        print(WHITE_BOX[1])

    if guess == SECRET[2]:
        print(GREEN_BOX[2])
    else:
        print(WHITE_BOX[2])

    if guess == SECRET[3]:
        print(GREEN_BOX[3])
    else:
        print(WHITE_BOX[3])
        
    if guess == SECRET[4]:
        print(GREEN_BOX[4])
    else:
        print(WHITE_BOX[4])

    if guess == SECRET[5]:
        print(GREEN_BOX[5])
    else:
        print(WHITE_BOX[5])
        

