"""
Jumping and variables
video: https://www.youtube.com/watch?v=2-DNswzCkqk&list=PLzMcBGfZo4-lp3jAExUCewBfMx3UZFkh5&index=2

1. constraing are where we can move
2. jumping
IF JUMPING: dont move left right
"""

import pygame
from pygame.locals import *

from rgb_color_dictionary import *

pygame.init()

#create window
win = pygame.display.set_mode((500,500))
#set windows title
pygame.display.set_caption("First Game")

#character variables
x = 50
y = 50
width = 40
height = 60
vel = 20

isJump = False
jumpCount = 10

#clock=pygame.time.Clock()
#main game loop
run = True
while run:

	pygame.time.delay(100) #this will be a clock for the game
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
	if keystate[pygame.K_DOWN] and y < 500 - height - vel:
		vy = vel

	if not isJump:
		#cant move off the left screen border
		if keystate[pygame.K_LEFT] and x > vel:
			vx = -vel
		#cant move off the right screen border
		if keystate[pygame.K_RIGHT] and x < 500 - width - vel:
			vx = vel

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
		else:
			isJump = False
			jumpCount = 10

	#diagonals must be slower for sq(2)= 1.414 pitagora
	if vx != 0 and vy != 0:
		vx /= 1.414
		vy /= 1.414

	x += vx
	y += vy

	#draw rectangle
	win.fill(BLACK)
	pygame.draw.rect(win,RED,(x,y,width,height))
	pygame.display.update()
