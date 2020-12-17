"""
website: https://techwithtim.net/tutorials/game-development-with-python/pygame-tutorial/pygame-animation/
Character Animation
video: https://www.youtube.com/watch?v=2-DNswzCkqk&list=PLzMcBGfZo4-lp3jAExUCewBfMx3UZFkh5&index=2

"""

import pygame
from pygame.locals import *

from rgb_color_dictionary import *

pygame.init()

#create window
win = pygame.display.set_mode((500,500))
#set windows title
pygame.display.set_caption("First Game")

#load images for animation
walkRight =[
pygame.image.load("R1.png"),
pygame.image.load("R2.png"),
pygame.image.load("R3.png"),
pygame.image.load("R4.png"),
pygame.image.load("R5.png"),
pygame.image.load("R6.png"),
pygame.image.load("R7.png"),
pygame.image.load("R8.png"),
pygame.image.load("R9.png")]

walkLeft =[
pygame.image.load("L1.png"),
pygame.image.load("L2.png"),
pygame.image.load("L3.png"),
pygame.image.load("L4.png"),
pygame.image.load("L5.png"),
pygame.image.load("L6.png"),
pygame.image.load("L7.png"),
pygame.image.load("L8.png"),
pygame.image.load("L9.png")]

bg = pygame.image.load("bg.jpg")
char = pygame.image.load("standing.png")

#defining clock for the game
clock=pygame.time.Clock()

#character variables
x = 50
y = 50
width = 40
height = 60
vel = 5

isJump = False
jumpCount = 10

left = False
right = False
walkCount = 0

def redrawGameWindow():
	global walkCount
	#draw background
	win.blit(bg,(0,0))
	#if we are walking. displaying 9 sprites, 3 per frame = 27
	#afte
	print(walkCount)
	if walkCount + 1 >=27:
		walkCount = 0

	if left:
		win.blit(walkLeft[walkCount//3],(x,y)) #integer division to get sprite picture index
		walkCount += 1

	elif right:
		win.blit(walkRight[walkCount//3],(x,y)) #integer division to get sprite picture index
		walkCount += 1

	else:
		win.blit(char,(x,y))

	pygame.display.update()

#main game loop
run = True
while run:
	#1st set time for the game
	#pygame.time.delay(100) #this will be a clock for the game
	clock.tick(27)

	keys = {'left':False,'right':False, 'up':False, 'down':False}

	for event in pygame.event.get(): #check for all events that are happening
		if event.type == pygame.QUIT:
			run = False
		if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
			run = False

	vx = 0
	vy = 0
	keystate = pygame.key.get_pressed()
	#straight moves with screen constraints
	#cant move up
	if keystate[pygame.K_UP] and y > vel:
		vy = -vel
	#cant move down
	elif keystate[pygame.K_DOWN] and y < 500 - height - vel:
		vy = vel

	#while jumping cant move left or right
	if not isJump:
		#cant move off the left screen border
		if keystate[pygame.K_LEFT] and x > vel:
			vx = -vel
			left = True
			right = False
		#cant move off the right screen border
		elif keystate[pygame.K_RIGHT] and x < 500 - width - vel:
			vx = vel
			left = False
			right = True
		#if right or left not pressed, reset movement
		else:
			left = False
			right = False
			walkCount = 0
		#-----------------jump---------------
		if keystate[pygame.K_SPACE]:
			isJump = True
	else:
		if jumpCount >= -10: # we jump for 10 pixels
			neg = 1
			if jumpCount < 0: #when we get to the top of jump
				neg = -1
			y -= (jumpCount ** 2) * 0.5 * neg
			jumpCount -= 1
			#if jumping than we are not walking left or right
			left = False
			right = False
			walkCount = 0
		else:
			isJump = False
			jumpCount = 10

	#diagonals must be slower for sq(2)= 1.414 pitagora
	if vx != 0 and vy != 0:
		vx /= 1.414
		vy /= 1.414

	x += vx
	y += vy

	redrawGameWindow()

