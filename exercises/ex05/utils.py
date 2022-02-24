"""File to implement my function skeletons."""

__author__ = "730401929"

input: list[int] = list()


def only_evens(input: list[int]) -> list[int]:
    """Return list of even numbers from given list."""
    evens: list[int] = list()
    i: int = 0 
    while i < len(input): 
        if input[i] % 2 == 0:
            evens.append(input[i])
        i += 1 
    return evens 


def sub(input: list[int], start: int, end: int) -> list[int]: 
    """Return list of numbers between start and end int of given list."""
    new: list[int] = list()
    if len(input) == 0 or start > len(input) or end <= 0:
        return new 
    if start < 0:
        start = 0 
    if end > len(input):
        end = len(input)
    while start < end:
        new.append(input[start])
        start += 1 
    
    return new 

def concat(first: list[int], second: list[int]):
    """Return list that adds second list to first list."""
    i: int = 0 
    new: list[int] = list()
    while i < len(first):
        new.append(first[i])
        i += 1 
    i = 0 
    while i < len(second):
        new.append(second[i])
        i += 1 
    return new 