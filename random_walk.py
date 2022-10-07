import turtle
import random

bim = turtle.Turtle()
bim.pensize(15)
bim.speed(0)
colors = ['blue', 'blue1', 'aquamarine3', 'bisque3', 'chartreuse3', 'SeaGreen3',
          'sienna4', 'salmon', 'SkyBlue', 'violet', 'turquoise']

directions = [0, 90, 180, 270]


def random_walk():
    bim.color(random.choice(colors))
    bim.forward(30)
    bim.seth(random.choice(directions))
    bim.forward(30)


move = True
while move:
    if bim.xcor() > -300 and bim.xcor() < 300 and bim.ycor() > -300 and bim.ycor() < 300:
        random_walk()
    else:
        bim.back(100)
        random_walk()


screen = turtle.Screen()
screen.exitonclick()
