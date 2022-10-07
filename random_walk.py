import turtle
import random

bim = turtle.Turtle()
bim.pensize(15)
bim.speed(0)
turtle.colormode(255)

colors = ['blue', 'blue1', 'aquamarine3', 'bisque3', 'chartreuse3', 'SeaGreen3',
          'sienna4', 'salmon', 'SkyBlue', 'violet', 'turquoise']

directions = [0, 90, 180, 270]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb


def random_walk():
    bim.color(random_color())
    bim.forward(30)
    bim.seth(random.choice(directions))
    bim.forward(30)


move = True
while move:
    if bim.xcor() > -300 and bim.xcor() < 300 and bim.ycor() > -300 and bim.ycor() < 300:
        random_walk()
    else:
        bim.back(180)
        random_walk()


screen = turtle.Screen()
screen.exitonclick()

# Python Tuples
# Tuples = (1, 3, 8)
# tuple is stone carved, you cant change the value. it does not support item assignment --> # Immutable
