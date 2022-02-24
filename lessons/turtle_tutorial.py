from turtle import Turtle, colormode, done 
colormode(255)
leo: Turtle = Turtle()
leo.penup()
leo.goto(-200, 150)
leo.pendown()
i: int = 0 
leo.begin_fill()
while i < 3:
    leo.forward(450)
    leo.right(120)
    i = i + 1
leo.pencolor("pink")
leo.fillcolor(40, 205, 255)
leo.end_fill()

bob: Turtle = Turtle()
bob.color(0, 0, 0)
bob.penup()
bob.goto(-200, 150)
bob.speed(50)

side_length: int = 450
i: int = 0 
while i < 10:
    bob.forward(side_length)
    leo.right(120)
    i = i + 1
    side_length = side_length * 2



done()
