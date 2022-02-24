"""Drawing of a mountain scene, sun, and ladybug."""

__author__ = "730401929"

from turtle import Turtle, done


def main() -> None: 
    """The entrypoint of my scene."""
    mount: Turtle = Turtle()
    mountain(mount, -450, -55, 300)
    mountain(mount, -400, -50, 400)
    mountain(mount, -200, -40, 300)
    mountain(mount, -50, -60, 475)
    grass()
    sun()
    ladybug()
    dot()
    done()


def mountain(mount: Turtle, x: float, y: float, size: float) -> None: 
    """Drawing mountains to include in mountain scene."""
    sides: int = 0 
    mount.penup()
    mount.goto(x, y)        
    mount.pendown()       
    mount.begin_fill()
    mount.pencolor("#714320")
    mount.fillcolor("#714320")
    while sides < 3:
        mount.forward(size)
        mount.left(120)
        sides += 1
    mount.end_fill()


def grass() -> None:
    """Drawing grass."""
    grass: Turtle = Turtle()
    sides: int = 0 
    grass.penup()
    grass.goto(-450, -50)
    grass.pendown()
    grass.begin_fill()
    grass.pencolor("#207122")
    grass.fillcolor("#207122")
    while sides < 4:
        grass.forward(1000)
        grass.right(90)
        sides += 1 
    grass.end_fill()


def sun() -> None: 
    """Drawing the sun."""
    sun: Turtle = Turtle()
    sun.penup()
    sun.goto(-100, 200)
    sun.pendown()
    sun.pensize(5)
    sun.begin_fill()
    sun.pencolor("#F58216")
    sun.fillcolor("#F5DE16")
    sun.circle(30)
    sun.end_fill()


def ladybug() -> None: 
    """Drawing a ladybug in the grass."""
    bug: Turtle = Turtle()
    bug.penup()
    bug.goto(40, -225)
    bug.pendown()
    bug.pensize(10)
    bug.begin_fill()
    bug.pencolor("#000000")
    bug.fillcolor("#D11A1A")
    bug.circle(75)
    bug.end_fill()
    bug.left(90)
    bug.forward(150)
    

def dot() -> None: 
    """This function adds dots to the ladybug."""
    dot: Turtle = Turtle()
    dot.penup()
    dot.goto(15, -195)
    dot.pendown()
    dot.fillcolor("#000000")
    dot.dot(30)
    dot.penup()
    dot.goto(0, -150)
    dot.pendown()
    dot.fillcolor("#000000")
    dot.dot(30)
    dot.penup()
    dot.goto(15, -110)
    dot.pendown()
    dot.fillcolor("#000000")
    dot.dot(30)
    dot.penup()
    dot.goto(65, -190)
    dot.pendown()
    dot.fillcolor("#000000")
    dot.dot(30)
    dot.penup()
    dot.goto(80, -150)
    dot.pendown()
    dot.fillcolor("#000000")
    dot.dot(30)
    dot.penup()
    dot.goto(65, -105)
    dot.pendown()
    dot.fillcolor("#000000")
    dot.dot(30)


if __name__ == "__main__":
    main()