from turtle import *

wn = Screen()
wn.setup(500,500)
turtle = Turtle()
turtle.speed("fastest")

step = 100
def draw_square(length,angle,a):
    if a<step:
        for b in range (0,4):
            turtle.forward(length+a-b)
            turtle.right(angle+b)
        draw_square(length+1,angle+1,a+1)

draw_square(100,90,0)
                                            