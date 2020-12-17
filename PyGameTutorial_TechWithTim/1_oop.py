"""
Basic Movement and Key Presses
video: https://www.youtube.com/watch?v=i6xMBig-pP4&list=PLzMcBGfZo4-lp3jAExUCewBfMx3UZFkh5

1. create a rectangle
2. move it by key pressed
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
vel = 5

class player(object):
	def __init__(self, x, y, vx, vy, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.vx = vx
		self.vy = vy
		self.vel = 5
		self.isJump = False
		self.jumpCount = 10
		self.left = False
		self.right = False
		self.up = False
		self.down = False
		self.walkCount = 0

	def draw(self,win):
		pygame.draw.rect(win,RED,(self.x,self.y,self.width,self.height)) #draw player

	def set_speed(self, vx, vy):
		red_cube.vx = vx
		red_cube.vy = vy


def redrawGameWindow():
	pygame.display.update()

#create a player
red_cube = player(x=50,y=50,vx=0,vy=0, width=40,height=60)

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

	red_cube.set_speed(0,0)	#cube not moving

	keystate = pygame.key.get_pressed()
	#straight moves
	if keystate[pygame.K_UP]:
		red_cube.vy = -5
	if keystate[pygame.K_DOWN]:
		red_cube.vy = 5
	if keystate[pygame.K_LEFT]:
		red_cube.vx = -5
	if keystate[pygame.K_RIGHT]:
		red_cube.vx = 5
	#diagonals must be slower for sq(2)= 1.414 pitagora
	if red_cube.vx != 0 and red_cube.vy != 0:
		red_cube.vx /= 1.414
		red_cube.vy /= 1.414

	red_cube.x += red_cube.vx
	red_cube.y += red_cube.vy
	#print(keys)

	win.fill(BLACK)	#draw background
	#pygame.draw.rect(win,RED,(x,y,width,height)) #draw player
	red_cube.draw(win)

	redrawGameWindow()
