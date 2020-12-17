"""Snake Game Python Tutorial
youtube video: https://www.youtube.com/watch?v=CD4qAhfFuLo
current time: 34:00
"""
import sys
import math
import random
import pygame
from pygame.locals import *
import tkinter as tk
from tkinter import messagebox

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
#-----------------------------------------------------------------------------------
class cube(object):
	"""
	"""
	rows = 20 #set number of rows
	w = 500 #set pixel screen width
	def __init__(self, start, dirnx=1, dirny=0, color = RED):
		self.pos = start
		self.dirnx = 1
		self.dirny = 0
		self.color = color

	def move(self,dirnx,dirny):
		"""
		move cube, by adding new direction to previous position
		"""
		self.dirnx = dirnx
		self.dirny = dirny
		self.pos = (self.pos[0]+self.dirnx, self.pos[1]+self.dirny)

	def draw(self,surface,eyes=False):
		"""
		drawing: convert x,y grid position to pixel position
		"""
		dis = self.w // self.rows #distance between x and y values
		#variables for easy coding
		i = self.pos[0] # row
		j = self.pos[1] # column
		#draw just a little bit less, so we draw inside of the square. and we dont cover grid.
		pygame.draw.rect(surface, self.color, (i*dis+1,j*dis+1,dis-2,dis-2 ))

		#draw eyes
		if eyes:
				centre = dis//2
				radius = 3
				circleMiddle = (i*dis+centre-radius, j*dis+8 ) #eye 1
				circleMiddle2 = (i*dis+dis-radius*2, j*dis+8 ) #eye 2
				pygame.draw.circle(surface, BLACK, circleMiddle, radius)
				pygame.draw.circle(surface, BLACK, circleMiddle2, radius)
#-----------------------------------------------------------------------------------
class snake(object):
	"""
	class for snake
	"""
	body = [] #list of cube objects
	turns = {} #dictionary of turns  ADDING A KEY OF-->
	# key = current position of snake head
	# value = direction of turn]
	def __init__(self,color,pos):
		self.color = color
		self.head = cube(pos)
		self.body.append(self.head) # snake starts with one cube = head
		self.dirnx = 0	#direction moving x 1, -1
		self.dirny = 1	#direction moving y 1, -1
	#---------------------------------------------------------------------
	def move(self):
		"""
		moving our snake in x,y thinking
		LEFT  	(self.dirnx=-1, self.dirny=0)
		RIGHT 	(self.dirnx=1, self.dirny=0)
		UP 		(self.dirnx=0, self.dirny=1)
		DOWN 	(self.dirnx=0, self.dirny=-1)
		"""
		for event in pygame.event.get():
			if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
				pygame.quit()
				sys.exit()

			keys = pygame.key.get_pressed()
			for key in keys:
				if keys[pygame.K_LEFT]:
					self.dirnx = -1
					self.dirny = 0
					# we mustremember where we turned, so other cubes can follow
					# add a new key
					#example - here we turned in thar way
					self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
				elif keys[pygame.K_RIGHT]:
					self.dirnx = 1
					self.dirny = 0
					self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
				elif keys[pygame.K_UP]:
					self.dirnx = 0
					self.dirny = -1
					self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
				elif keys[pygame.K_DOWN]:
					self.dirnx = 0
					self.dirny = 1
					self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

		#look trough all position of snake
		#we get the index=i and the cube=c of body
		for i, c in enumerate(self.body):
			p = c.pos[:]
			#for each of the sube, we grab position and check turn
			#if this position in turns, than we move
			if p in self.turns:
				turn = self.turns[p]
				#here we store direction where to move
				c.move(turn[0],turn[1])
				#if we are on the last cube of the snake, remove the turn, we finished it
				if i == len(self.body)-1:
					self.turns.pop(p)

			else:	#CHECK IF WE REACHED EDGE OF THE SCREEN
				#if MOVE LEFT & we are at the left side of screen
				if (c.dirnx == -1) and (c.pos[0] <= 0):
					c.pos = (c.rows-1,c.pos[1])
					#c.pos = (c.rows-1,c.pos[1])
				#if MOVE RIGHT & we are at the left side of screen
				elif (c.dirnx == 1) and (c.pos[0] >= c.rows-1):
					c.pos = (0,c.pos[1])
				#if MOVE DOWN & we are at the left side of screen
				elif (c.dirny == 1) and (c.pos[1] >= c.rows-1):
					c.pos = (c.pos[0],0)
				#if MOVE UP & we are at the left side of screen
				elif (c.dirny == -1) and (c.pos[1] <= 0):
					c.pos = (c.pos[0],c.rows-1)
				#normal move of cube
				else:
					c.move(c.dirnx,c.dirny)
	#---------------------------------------------------------------------
	def reset(self,pos):
		pass

	#---------------------------------------------------------------------
	def addCube(self):
		"""
		Figure out where is tail, and add a cube after it
		"""
		"""
		tail = self.body[-1] #last element in list is tail
		dx = tail.dirnx
		dy = tail.dirny

		#check in which direction is tail movin, so we know if we add it to left,right,up,down
		#we append a new cube to the body, that has one less position that the tail
		#are we moving right, append to left
		if dx == 1 and dy == 0:
			self.body.append(cube((tail.pos[0]-1,tail.pos[1]))

		#are we moving left, append to right
		#if dx == -1 and dy == 0:
		#	self.body.append(cube((tail.pos[0]+1,tail.pos[1]))
		#are we moving up, append to down
		#if dx == 0 and dy == 1:
		#	self.body.append(cube((tail.pos[0],tail.pos[1]-1))
		#are we moving down, append to up
		#if dx == 0 and dy == -1:
		#	self.body.append(cube((tail.pos[0],tail.pos[1]+1))

		#if we just leave it like this. the cube is not moving
		#add it moving
		self.body[-1].dirnx = dx
		self.body[-1].dirny = dy
		"""
		tail = self.body[-1]
		dx, dy = tail.dirnx, tail.dirny

		if dx == 1 and dy == 0:
			self.body.append(cube((tail.pos[0]-1,tail.pos[1])))
		elif dx == -1 and dy == 0:
			self.body.append(cube((tail.pos[0]+1,tail.pos[1])))
		elif dx == 0 and dy == 1:
			self.body.append(cube((tail.pos[0],tail.pos[1]-1)))
		elif dx == 0 and dy == -1:
			self.body.append(cube((tail.pos[0],tail.pos[1]+1)))

		self.body[-1].dirnx = dx
		self.body[-1].dirny = dy

	#---------------------------------------------------------------------
	def draw(self,surface):
		for index, cube in enumerate(self.body):
			#check where to draw eyes for snake head
			if index == 0:
				cube.draw(surface,True) #with eyes
			else:
				cube.draw(surface,False) #without eyes

#-----------------------------------------------------------------------------------
def drawGrid(w,rows,surface):
	"""
	This function draws a square grid on main display
	"""
	#distance between grid lines
	sizeBtwn = w // rows
	x = 0
	y = 0

	#create grid by drawing lines
	for l in range(rows):
		x = x + sizeBtwn
		y = y + sizeBtwn
		#vertical lines
		pygame.draw.line(surface, WHITE, (x,0), (x,w))
		#horizontal lines
		pygame.draw.line(surface, WHITE, (0,y), (w,y))
#-----------------------------------------------------------------------------------
def redrawWindow(surface):
	global rows, width, s, snack
	#background
	surface.fill(BLACK)
	s.draw(surface)
	snack.draw(surface)
	#draw grid
	drawGrid(width, rows, surface)
	#update display
	pygame.display.update()
#-----------------------------------------------------------------------------------
def randomSnack(rows,item):
	"""
	create random snack cubes:
	we must be sure we dont put a snack on top of the snake
	"""
	#global rows
	positions = item.body

	while True:
		x = random.randrange(rows)
		y = random.randrange(rows)
		#we get a list of filtered list and check if and of the positions
		#are the current positions of the snake
		#if snack position is equal to the *random(x,y) than repeat the loop
		if len(list(filter(lambda z:z.pos ==(x,y), positions))) > 0:
			continue
		else:
			break
	return (x,y) #return snack position that is not on the snake
#-----------------------------------------------------------------------------------
def message_box(subject,content):
	pass
#-----------------------------------------------------------------------------------
def key_events():
	pass

#directions = {"right":(1,0), "left":(0,-1), "up":(0,-1), "down":(0,1)}
#-----------------------------------------------------------------------------------
def main():
	global width, rows, s, snack
	#---------------game initialization---------------------------
	#create game display
	width = 500
	rows = 20
	win = pygame.display.set_mode((width, width)) #square display
	#snake start position
	s = snake(color=RED, pos=(10,10))
	snack = cube(randomSnack(rows,s), color = GREEN)
	print(snack.pos)
	clock = pygame.time.Clock()
	flag = True
	FPScount = 0
	print(FPScount)
	redrawWindow(win)
	#-----------------------continuous game loop-------------
	while flag:
		#pygame.time.delay(50)
		clock.tick(10)	#game max speed 10 FPS
		s.move()
		#check if the snack was eaten. if it was
		if s.body[0].pos == snack.pos:
			s.addCube() #add new cube to snake
			snack = cube(randomSnack(rows,s), color = GREEN) #generate new snack cube
		#------------debug fps counter---------
		FPScount += 1
		print(f'FPScount:{FPScount}')
		#--------------------------------------
		redrawWindow(win)
#rows = 0
#w = 0
#h = 0

#cube.rows = rows
#cube.w = w
main()
pygame.quit()
sys.exit()