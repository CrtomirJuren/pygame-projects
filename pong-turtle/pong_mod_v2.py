"""
Simple pong in python 3 for begginers

tutorial series: https://www.youtube.com/playlist?list=PLlEgNdBJEO-kXk2PyBxhSmo84hsO3HAz2
"""

import turtle
import time
import random
import winsound
import os
import winsound

filename = 'C:/Users/crtom/Documents/py-learn/pygame/pong-turtle/sound.wav'

win_score = int(input("Set score to win:"))

#file = "sound.wav"
#os.system("C:\Users\crtom\Documents\py-learn\pygame\pong-turtle" + file)

#pygame.init()
#pygame.mixer.Sound('sound.wav').play()
#pygame.mixer.Sound('sfx_sounds_interaction7.wav').play()
#winsound.PlaySound('sound.wav', winsound.SND_FILENAME)
#"sfx_sounds_interaction7.wav"
#winsound.PlaySound('fx_sounds_interaction7.wav', winsound.SND_FILENAME)
wn = turtle.Screen()
wn.title("Pong by @CrtomiJuren")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

KEY_REPEAT_RATE = 10  # in milliseconds for

score_a = 0
score_b = 0

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

ball.dx = 4 #speed
ball.dy = 4

print(random.choice([-1,1]))

#write scoreboard
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A:  0  Player B:  0", align="center", font=("courier",24,"normal"))

# Functions
def paddle_a_up():
	y = paddle_a.ycor() #method, returns y coor
	#constraing of paddle movement
	print(y)
	if y < 240:
		y+= 20 #add 20 pixels to y coor
	paddle_a.sety(y)

def paddle_a_down():
	y = paddle_a.ycor() #method, returns y coor
	if y > -240:
		y -= 20 #add 20 pixels to y coor
	paddle_a.sety(y)

def paddle_b_up():
	y = paddle_b.ycor() #method, returns y coor
	if y < 240:
		y+= 20 #add 20 pixels to y coor
	paddle_b.sety(y)

def paddle_b_down():
	y = paddle_b.ycor() #method, returns y coor
	if y > -240:
		y -= 20 #add 20 pixels to y coor
	paddle_b.sety(y)

def play_bounce_sound():
	#winsound.PlaySound(filename, winsound.SND_FILENAME)
	#os.system("C:/Users/crtom/Documents/py-learn/pygame/pong-turtle/sound.wav&")
	winsound.PlaySound(filename,winsound.SND_ASYNC)

"""
#keyboard biding
wn.listen() #listen for key inputs
wn.onkey(paddle_a_up,"w") #when user press "w" call function paddle_a_up

wn.onkey(paddle_a_down,"s") #when user press "w" call function paddle_a_up
wn.onkey(paddle_b_up,"Up") #when user press "w" call function paddle_a_up
wn.onkey(paddle_b_down,"Down") #when user press "w" call function paddle_a_up

wn.onkey(lambda:print("t"),"t") #when user press "w" call function paddle_a_up
wn.onkeyrelease(lambda:print("t"),"t") #when user press "w" call function paddle_a_up
"""
# Define functions for each arrow key
def go_w():
	paddle_a_up()
	#print("w")
	if repeating:
		wn.ontimer(go_w, KEY_REPEAT_RATE)

def go_s():
	paddle_a_down()
	#print("s")
	if repeating:
		wn.ontimer(go_s, KEY_REPEAT_RATE)

def go_up():
	paddle_b_up()
	#print("up")
	if repeating:
		wn.ontimer(go_up, KEY_REPEAT_RATE)

def go_down():
	paddle_b_down()
	#print("down")
	if repeating:
		wn.ontimer(go_down, KEY_REPEAT_RATE)

def start_repeat(func):
	global repeating
	repeating = True
	func()

def stop_repeat():
	global repeating
	repeating = False

repeating = False

# Tell the program which functions go with which keys
wn.onkeypress(lambda: start_repeat(go_w), 'w')
wn.onkeyrelease(stop_repeat, 'w')

wn.onkeypress(lambda: start_repeat(go_s), 's')
wn.onkeyrelease(stop_repeat, 's')

wn.onkeypress(lambda: start_repeat(go_up), 'Up')
wn.onkeyrelease(stop_repeat, 'Up')

wn.onkeypress(lambda: start_repeat(go_down), 'Down')
wn.onkeyrelease(stop_repeat, 'Down')

# Tell the screen to listen for key presses
wn.listen()

# main game loop
GameOver = False
while not GameOver:
	wn.update() #updates screen
	time.sleep(0.01)

	#move the ball
	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)

	#border checking
	#----------top sides bounce--------
	#top side
	if ball.ycor() > 290:
		ball.sety(290)
		ball.dy *= -1 #reverse direction of the ball
		play_bounce_sound()

	#bottom side
	elif ball.ycor() < -285:
		ball.sety(-285)
		ball.dy *= -1 #reverse direction of the ball
		play_bounce_sound()

	#----------bot sides finish the game--------
	#right side
	if ball.xcor() > 390:
		ball.goto(0,0) #put ball back to the start
		ball.dx *= -1 #reverse direction of the ball
		score_a += 1
		pen.clear()
		pen.write(f"Player A:  {score_a}  Player B:  {score_b}", align="center", font=("courier",24,"normal"))

	#left side
	elif ball.xcor() < -390:
		ball.goto(0,0) #put ball back to the start
		ball.dx *= -1 #reverse direction of the ball
		score_b += 1
		pen.clear()
		pen.write(f"Player A:  {score_a}  Player B:  {score_b}", align="center", font=("courier",24,"normal"))

	#Paddle and ball collisions
	#if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor()+50 and ball.ycor()>paddle_b.ycor()-50)
	paddle_b_y_coll = ((ball.ycor() < paddle_b.ycor()+50) and(ball.ycor()>paddle_b.ycor()-50))
	paddle_a_y_coll = ((ball.ycor() < paddle_a.ycor()+50) and(ball.ycor()>paddle_a.ycor()-50))
	right_coll = ((ball.xcor() > 340) and (ball.xcor() < 350))
	left_coll = ((ball.xcor() < -340) and (ball.xcor() > -350))

	if paddle_b_y_coll and right_coll:
		ball.setx(340)
		ball.dx *= -1 #reverse direction of the ball
		play_bounce_sound()

	if paddle_a_y_coll and left_coll:
		ball.setx(-340)
		ball.dx *= -1 #reverse direction of the ball
		play_bounce_sound()

	if score_a >= win_score:
		GameOver = True
		print("Player A won")

	if score_b >= win_score:
		GameOver = True
		print("Player B won")
	#debug
	#print (f'ball.xcor():{ball.xcor()}')
	#print (f'ball.ycor():{ball.ycor()}')
	#print (f'paddle_b.ycor():{paddle_b.ycor()}')

	#diff = ball.ycor() - paddle_b.ycor()
	#print (f'diff:{diff}')
