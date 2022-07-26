from turtle import Screen
from paddle import paddle
from ball import Ball
from scoreboard import Scoreboard
import time



p1_position = (350,0)
p2_position = (-350,0)

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)


r_paddle = paddle((350,0))
l_paddle = paddle(p2_position)


screen.listen()
screen.onkey(r_paddle.goUp,'Up')
screen.onkey(r_paddle.goDown, 'Down')

screen.onkey(l_paddle.goUp,'w')
screen.onkey(l_paddle.goDown,'s')

ball = Ball()
score = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < - 280:
        ball.bounce_y()

    
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()


    if ball.xcor() > 380:
        ball.miss()
        score.l_point()
        
        
    if ball.xcor() < -380:
        ball.miss()
        score.r_point()
        
        
    
screen.exitonclick()