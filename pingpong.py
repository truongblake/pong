import turtle
import random

class Paddle:
   def __init__(self,x,y):
      self.a = turtle.Turtle()
      self.a.speed(0)
      self.a.shape("square")
      self.a.shapesize(stretch_wid=5,stretch_len=1)
      self.a.color("white")
      self.a.penup()
      self.a.goto(x,y)
      self.score = 0

class Ball:
    def __init__(self,x = 0,y = 0,dx = 2,dy = 2):
        self.ball = turtle.Turtle()
        self.ball.speed(0)
        self.ball.shape("square")
        self.ball.color("white")
        self.ball.penup()
        self.ball.goto(x,y)
        self.dx = dx
        self.dy = dy
    
    def move(self):
        
        self.ball.setx(self.ball.xcor() + self.dx)
        self.ball.sety(self.ball.ycor() + self.dy)

    def collision_check(self,paddle):
        if(self.ball.ycor() + self.dy > 290 or self.ball.ycor() + self.dy < -290):
            self.dy *= -1
        if(self.ball.xcor() + self.dx == paddle.a.xcor() and self.ball.ycor() < paddle.a.ycor() + 60 and self.ball.ycor() > paddle.a.ycor() - 60 ):
            self.dx *= -1

    def check_win(self, paddle_a, paddle_b, pen):
        if(self.ball.xcor() > 400 or self.ball.xcor() < -400):
            pen.clear()
            if self.ball.xcor() > 400:
                paddle_a.score += 1
            else:
                paddle_b.score += 1
            pen.up()
            pen.goto(100,0)
            pen.down()
            pen.write(paddle_b.score,font=("Courier", 24, "normal"))
            pen.up() 
            pen.goto(-100,0)
            pen.down()
            pen.write(paddle_a.score,font=("Courier", 24, "normal"))
            self.dx = random.choice([-2,2])
            self.dy = random.choice([-2,2])
            self.ball.setx(0)
            self.ball.sety(random.randint(-280,280))
            return True
        else:
            return False