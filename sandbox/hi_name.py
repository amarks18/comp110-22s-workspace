"""A function that says hi to its friends."""

__author__ = "730401929"

def say_hi(int) -> str:
    """Uses naming function to say hi."""
    name = what_name(int)
    res = "Hi " + name
    return res


def what_name(choice) -> str:
    """Chooses who to say hi to."""
    if choice == 1:
        result = "Anna"
    else:
        result = "Josh"
    return result
