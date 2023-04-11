def main() -> None:
    """The entry point of the program and main game loop."""
    number_turns = number_turns + 1
    print(f"You won in {number_turns}/6 turns! ")


print (f"===Turn {number_turns + 1}/6 ===")





 while single_character in range (0, len(word)):
        if word[single_character] == SECRET[single_character]:
            result = result + GREEN_BOX
        else:  
            while single_character in range (0, len(word)):
                if guess_input[single_character] != SECRET[single_character] and guess_input[single_character] == SECRET[single_character]:
                    playing = False
            if playing == True:
                result = result + YELLOW_BOX 
            else:
                result = result + WHITE_BOX 
        return guess_input