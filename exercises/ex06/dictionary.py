"""File to create functions using dictionaries."""

__author__ = "730401929"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Function that inverts the keys and values in a dictionary."""
    new_invert: dict[str, str] = {}
    if input == {}: 
        raise KeyError 
    for key in input:
        if input[key] in new_invert: 
            raise KeyError 
        else: 
            new_invert[input[key]] = key 
    return new_invert


def favorite_color(input: dict[str, str]) -> str:
    """Function that returns a str with the color that appears most frequently in the dictionary."""
    if input == {}:
        raise KeyError 
    new: dict[str, int] = dict()
    number: int = 0
    color: str = ""
    for key in input: 
        if input[key] in new:
            new[input[key]] += 1 
        else:
            new[input[key]] = 1 
    for key in new: 
        if new[key] > number: 
            number = new[key]
            color = key 
    return(color)


def count(input: list[str]) -> dict[str, int]:
    """Function that returns a dictionary where each key is associated with the number of times it is found in the input list."""
    if input == {}:
        raise KeyError
    new: dict[str, int] = {}
    i: int = 0 
    while i < len(input):
        if input[i] in new:
            new[input[i]] += 1 
        else:
            new[input[i]] = 1 
        i += 1 
    return new