"""
Simple pong in python 3 for begginers

tutorial series: https://www.youtube.com/playlist?list=PLlEgNdBJEO-kXk2PyBxhSmo84hsO3HAz2
"""

import turtle

wn = turtle.Screen()
wn.title("Pong by @TokyoEdTech")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed() #sets the speed of animation to max
paddle_a.shape("square") #default is 20x20 pixels
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len = 1) # strech the square
paddle_a.penup()
paddle_a.goto(-350,0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed() #sets the speed of animation to max
paddle_b.shape("square") #default is 20x20 pixels
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len = 1) # strech the square
paddle_b.penup()
paddle_b.goto(350,0)

# Ball
ball = turtle.Turtle()
ball.speed() #sets the speed of animation to max
ball.shape("square") #default is 20x20 pixels
ball.color("white")
ball.penup()
ball.goto(0,0)

# Functions
def paddle_a_up():
	y = paddle_a.ycor() #method, returns y coor
	y+= 20 #add 20 pixels to y coor
	paddle_a.sety(y)

def paddle_a_down():
	y = paddle_a.ycor() #method, returns y coor
	y -= 20 #add 20 pixels to y coor
	paddle_a.sety(y)

def paddle_b_up():
	y = paddle_b.ycor() #method, returns y coor
	y+= 20 #add 20 pixels to y coor
	paddle_b.sety(y)

def paddle_b_down():
	y = paddle_b.ycor() #method, returns y coor
	y -= 20 #add 20 pixels to y coor
	paddle_b.sety(y)

#keyboard biding
wn.listen() #listen for key inputs
wn.onkey(paddle_a_up,"w") #when user press "w" call function paddle_a_up
wn.onkey(paddle_a_down,"s") #when user press "w" call function paddle_a_up
wn.onkey(paddle_b_up,"Up") #when user press "w" call function paddle_a_up
wn.onkey(paddle_b_down,"Down") #when user press "w" call function paddle_a_up


# main game loop
while True:
	wn.update() #updates screen