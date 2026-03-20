import turtle

wn = turtle.Screen()
wn.title("Pong by @elena")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)





# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("blue")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()   
ball.goto(0, 0)
ball.dx = 0.13
ball.dy = -0.13

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))
score_a = 0
score_b = 0

# Function to move paddle A up
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

# Function to move paddle A down
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

# Function to move paddle B up
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

# Function to move paddle B down
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.listen()
wn.onkeypress(paddle_a_down, "s")
wn.listen()
wn.onkeypress(paddle_b_up, "Up")
wn.listen()
wn.onkeypress(paddle_b_down, "Down")
# Main game loop
while True:
    wn.update()


    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Borders
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1 

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        
        #this means that if the ball goes past the right border (xcor > 390), it will reset to the center (0, 0), reverse its x-direction (ball.dx *= -1), and increment Player A's score by 1. Then, it clears the pen and writes the updated scores for both players at the top of the screen.

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

#this means that if the ball goes past the left border (xcor < -390), it will reset to the center (0, 0), reverse its x-direction (ball.dx *= -1), and increment Player B's score by 1. Then, it clears the pen and writes the updated scores for both players at the top of the screen.

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
     
     #this means that if the ball is within the x-coordinates of the right paddle (between 340 and 350) and within the y-coordinates of the right paddle (between paddle_b.ycor() + 50 and paddle_b.ycor() - 50), then the ball will bounce back by reversing its x-direction (ball.dx *= -1) and setting its x-coordinate to 340 to prevent it from going past the paddle.
    
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
    #this means that if the ball is within the x-coordinates of the left paddle (between -340 and -350) and within the y-coordinates of the left paddle (between paddle_a.ycor() + 50 and paddle_a.ycor() - 50), then the ball will bounce back by reversing its x-direction (ball.dx *= -1) and setting its x-coordinate to -340 to prevent it from going past the paddle.
