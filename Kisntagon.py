from turtle import *
speed(100)
l = 25
def ntagon(n, sideLength):
    for i in range(n):
        forward(sideLength)
        left(360.0/n)
        if i == (n-1) and sideLength > 5 and n > 3:
            ntagon(n-1, sideLength)


def draw():
    for x in range(4):
        ntagon(8, l)
        forward(l)
        right(90)
def move():
    penup()
    forward(l)
    left(45)
    forward(l)
    right(45)
    forward(l)
    left(90)
    forward(2*l)
    right(45)
    forward(l)
    right(45)
    pendown()


def turn():
    right(90)
    forward(l)
    left(180)

# draw()
# move()
# draw()
# turn()
# move()
# draw()
# turn()
# move()
# draw()
# move()
# draw()
# turn()
# move()
# draw()
# move()
# draw()


x = 1.0
draw()
for i in range(100):
    for y in range(int(x)):
        move()
        draw()
    turn()
    x+=.5

input()
