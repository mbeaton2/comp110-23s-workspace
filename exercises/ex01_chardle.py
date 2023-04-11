"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730480912"

word_guesser: str = input("Enter a 5-character word: ")
if len(word_guesser) != int(5):
    print("Error: Word must contain 5 characters")
    quit()

letter_guesser: str = input("Enter a single character: ")
if len(letter_guesser) != int(1):
    print("Error: Character must be a single character")
    quit()

counter_variable: int = 0

print("Searching for " + letter_guesser + " in " + word_guesser)

if letter_guesser != word_guesser: 
    print("No instance of " + letter_guesser + " found in " + word_guesser)

if letter_guesser == word_guesser[0]:
    print(letter_guesser + " found at index 0")
    counter_variable = counter_variable + 1
    print(str (counter_variable) + " instance of " + letter_guesser + " found in " + word_guesser)

if letter_guesser == word_guesser[1]:
    print(letter_guesser + " found at index 1")
    counter_variable = counter_variable + 1
    print(str(counter_variable) + " instance of " + letter_guesser + " found in " + word_guesser)

if letter_guesser == word_guesser[2]:
    print(letter_guesser + " found at index 2 and 3")
    counter_variable = counter_variable + 1
    print(str(counter_variable) + " instances of " + letter_guesser + " found in " + word_guesser)

if letter_guesser == word_guesser[3]:
    print(letter_guesser + " found at index 2 and 3")
    counter_variable = counter_variable + 1
    print(str(counter_variable) + " instances of " + letter_guesser + " found in " + word_guesser)

if letter_guesser == word_guesser[4]:
    print(letter_guesser + " found at index 4")
    counter_variable = counter_variable + 1
    print(str(counter_variable) + " instance of " + letter_guesser + " found in " + word_guesser)