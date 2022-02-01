"""Exercise 02 - One-Shot Wordle"""

__author__ = "730401929"

from tkinter import FALSE
from xml.etree.ElementPath import prepare_descendant


secret: str = "python"
guess: str = input("What is your 6-letter guess?")
counter: int = 6

while len(guess) != 6:
    guess: str = input("That was not 6 letters! Try again:")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
length: str = guess[0]
maximum: int = 6
i: int = 0
help: str = ""

present: bool = FALSE
alternate: int = 0

# while i < maximum:
#     if guess[i] == secret[i]:
#         help = help + GREEN_BOX 
#     if guess[i] == secret[alternate]:
#         present = "True"
#         help = help + YELLOW_BOX
#         alternate = alternate + 1
#     else:
#         help = help + WHITE_BOX
while i < maximum: 
    if guess[i] == secret[i]:
        help = help + GREEN_BOX
    else:
        while present == False and alternate < maximum: 
            if secret[alternate] == guess[i]:
                present = True
            else:
                alternate = alternate + 1 
        if present:
            help = help + YELLOW_BOX
        else:
            help = help + WHITE_BOX 
    alternate = 0
    present = False
    i = i + 1 
print(help)

if guess == "python":
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")





    







