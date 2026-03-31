from turtle import *
import time
import random

screen = Screen()
screen.title("Pong by @elena")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

def draw_paddle(x, y, colour):
    paddle = Turtle()
    paddle.speed(0)
    paddle.shape("square")
    paddle.color(colour)
    paddle.shapesize(stretch_wid=5, stretch_len=1)
    paddle.penup()
    paddle.goto(x, y)
    return paddle

paddle_a = draw_paddle(-350, 0, "red")
paddle_b = draw_paddle(350, 0, "blue")

def make_ball():
    b = Turtle()
    b.speed(0)
    b.shape("circle")
    b.color("white")
    b.penup()
    b.goto(0, 0)
    b.dx = 3
    b.dy = 3
    return b

ball = make_ball()

def reset_ball():
    ball.goto(0, 0)
    ball.dx = random.choice([-3, 3])
    ball.dy = random.choice([-3, 3])

pen = Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)

score_a = 0
score_b = 0
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

def paddle_a_up():
    y = paddle_a.ycor()
    if y < 250:
        paddle_a.sety(y + 20)

def paddle_a_down():
    y = paddle_a.ycor()
    if y > -250:
        paddle_a.sety(y - 20)

def paddle_b_up():
    y = paddle_b.ycor()
    if y < 250:
        paddle_b.sety(y + 20)

def paddle_b_down():
    y = paddle_b.ycor()
    if y > -250:
        paddle_b.sety(y - 20)

screen.listen()
screen.onkeypress(paddle_a_up, "w")
screen.onkeypress(paddle_a_down, "s")
screen.onkeypress(paddle_b_up, "Up")
screen.onkeypress(paddle_b_down, "Down")

max_score = 7

while True:
    screen.update()
    time.sleep(0.01)

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}",
                  align="center", font=("Courier", 24, "normal"))
        reset_ball()

    if ball.xcor() < -390:
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}",
                  align="center", font=("Courier", 24, "normal"))
        reset_ball()

    if (340 < ball.xcor() < 350) and (paddle_b.ycor() - 50 < ball.ycor() < paddle_b.ycor() + 50):
        ball.setx(340)
        ball.dx *= -1

    if (-350 < ball.xcor() < -340) and (paddle_a.ycor() - 50 < ball.ycor() < paddle_a.ycor() + 50):
        ball.setx(-340)
        ball.dx *= -1

    if score_a >= max_score:
        pen.clear()
        pen.write("Player A wins congratulations!", align="center", font=("Courier", 36, "normal"))
        break

    if score_b >= max_score:
        pen.clear()
        pen.write("Player B wins congratulations!", align="center", font=("Courier", 36, "normal"))
        break
