"""
Basic Movement and Key Presses
video: https://www.youtube.com/watch?v=i6xMBig-pP4&list=PLzMcBGfZo4-lp3jAExUCewBfMx3UZFkh5

1. create a rectangle
2. move it by key pressed
"""

import pygame
from pygame.locals import *

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
vel = 5


#clock=pygame.time.Clock()
#main game loop
run = True
while run:

	pygame.time.delay(100) #this will be a clock for the game

	for event in pygame.event.get(): #check for all events that are happening
		if event.type == pygame.QUIT:
			run = False
		if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
			run = False

	vx = 0
	vy = 0
	keystate = pygame.key.get_pressed()
	#straight moves
	if keystate[pygame.K_UP]:
		vy = -5
	elif keystate[pygame.K_DOWN]:
		vy = 5
	elif keystate[pygame.K_LEFT]:
		vx = -5
	elif keystate[pygame.K_RIGHT]:
		vx = 5

	x += vx
	y += vy

	#draw rectangle
	win.fill((0,0,0))
	pygame.draw.rect(win,(255,0,0),(x,y,width,height))
	pygame.display.update()
