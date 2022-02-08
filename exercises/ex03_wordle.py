"""Exercise 03 - Wordle."""

__author__ = "730401929"


def contains_char(word: str, char: str) -> bool:
    """Checks to see if the single character is in the word given as the first string."""
    assert len(char) == 1
    i: int = 0
    maximum: int = len(word)
    while i < maximum:
        if char == word[i]:
            return True
        i = i + 1
    return False 


def emojified(guess: str, secret: str) -> str:
    """Returns string of emojis that codify player's guess compared to the secret word."""
    assert len(guess) == len(secret)
    help: str = ""
    i: int = 0
    maximum: int = len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    while i < maximum:
        if contains_char(secret,guess[i]) == False:
            help = help + WHITE_BOX
        else:
            if guess[i] == secret[i]:
                help = help + GREEN_BOX
            else:
                help = help + YELLOW_BOX 
        i = i + 1
    return help


def input_guess(length: int) -> str:
    """Checks that the length of the guessed word matches the expected length."""
    guess: str = input("Enter a " + str(length) + " character word: ")
    while len(guess) != length:  
        guess = input("That wasn't " + str(length) + " chars! Try again: ")   
    return guess 


def main() -> None:
    """"The entrypoint of the program and main game loop."""
    secret: str = "codes"
    turn: int = 1
    length: int = 5
    correct: bool = False
    while turn <7 and correct == False: 
        print("=== Turn " + str(turn) + "/6 ===")
        guess: str = input_guess(length)
        if guess == secret:
            print(emojified(guess, secret))
            print("You won in " + str(turn) +"/6 turns!")
            correct = True
        else: 
            print(emojified(guess, secret))
        turn = turn + 1
    print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()





       