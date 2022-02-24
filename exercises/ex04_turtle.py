"""Drawing of the Pi Beta Phi House."""

__author__ = "730401929"

from turtle import Turtle, colormode, done, color

def main() -> None: 
    """The entrypoint of my scene."""
    mountain()
    done()

def mountain() -> None: 
    """Drawing mountains to include in mountain scene."""
    mount: Turtle = Turtle()
    sides: int = 0 
    count: int = 1
    while count < 4:
        coord: int = -450
        #mount.penup()
        mount.goto(coord, -50)
        #mount.pendown()       
        mount.begin_fill()
        mount.pencolor("#714320")
        mount.fillcolor("#714320")
        while sides < 3:
            mount.forward(450)
            mount.left(120)
            sides += 1
        coord += 150
        mount.end_fill()
        count += 1

if __name__ == "__main__":
    main()
