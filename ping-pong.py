from turtle import *


def draw_paddle(paddle):
    penup()
    goto(paddle[0], paddle[1])
    pendown()
    begin_fill()
    for _ in range(2):
        forward(paddle[2])
        left(90)
        forward(paddle[3])
        left(90)
    end_fill()
draw_paddle((0, 0, 100, 20))
done()
