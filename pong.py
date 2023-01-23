import turtle 
import pingpong
import random

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("Black")
wn.setup(width=800,height=600)
wn.tracer(0)

paddle_a = pingpong.Paddle(-350,0)
paddle_b = pingpong.Paddle(350,0)

pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")

ball = pingpong.Ball(0,0,random.choice([-2,2]),random.choice([-2,2]))

wn.listen()

def paddle_a_up():
    if paddle_a.a.ycor() + 20 < 280:
        y = paddle_a.a.ycor()
        y += 20
        paddle_a.a.sety(y)

def paddle_a_down():
    if paddle_a.a.ycor() - 20 > -260:
        y = paddle_a.a.ycor()
        y -= 20
        paddle_a.a.sety(y)

def paddle_b_up():
    if paddle_b.a.ycor() + 20 < 280:
        y = paddle_b.a.ycor()
        y += 20
        paddle_b.a.sety(y)

def paddle_b_down():
    if paddle_b.a.ycor() - 20 > -260:
        y = paddle_b.a.ycor()
        y -= 20
        paddle_b.a.sety(y)

wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

while True:
    wn.update()
    ball.check_win(paddle_a, paddle_b,pen)
    ball.collision_check(paddle_a)
    ball.collision_check(paddle_b)
    ball.move()

