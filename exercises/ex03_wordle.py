"""Structured Wordle"""

__author__= "730480912"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

def contains_char(word: str, single_character: str) -> bool:
        """Letter of the second string is found anywhere in the first string"""
        index: int = 0 
        assert len(single_character) == 1
        while index < len(word):
            if word[index] == single_character:
                return True
            else:
                if word[index] != single_character:
                    index = index + 1
        return False
                
def emojified(guess: str, SECRET: str) -> str:
        result: str = "" 
        """Concatenating boxes for matching and non-matching letters"""
        assert len(guess) == len(SECRET)
        index: int = 0 
        while  index < len(SECRET):
            if guess[index] == SECRET[index]:
                result = result + GREEN_BOX
            else:
                if contains_char(SECRET, guess[index])== True: 
                    result = result + YELLOW_BOX
        else: 
            if contains_char(SECRET, guess[index])== False: 
                result = result + WHITE_BOX
                index = index + 1
        return emojified 

def input_guess(expected_integer: int) -> str:
        """Length of guess attempting to equal length of secret"""
        expected_integer: str = input(f"Enter a {expected_integer}-character word: ")
        if len(guess) != expected_integer:
            guess = input(f"That wasn't {expected_integer} chars! Try again: ")
        return guess

def main() -> None:
    """The entrypoint of the program and main game loop"""
    SECRET: str = "codes"
    guess: bool = False 
    current_turn: int = 1
    number_turns: int = 6
    while number_turns <= current_turn and guess == False: 
        print(f"===Turn {current_turn}/{number_turns}===")
        guess: str = input_guess(len(SECRET))
        boxes: str = emojified(guess, SECRET)
        print(boxes)

        if guess == SECRET:
            print(f"You won in {current_turn}/{number_turns} turns! ")
            guess == True 
            
        else:
            current_turn = current_turn + 1
    if current_turn > number_turns and guess == False:
        print(f"X/{number_turns} -Sorry, try again tomorrow! ")
    return main

if __name__ == "__main__":
    main()