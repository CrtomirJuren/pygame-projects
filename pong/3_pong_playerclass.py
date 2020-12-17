import sys
import math
import random
import pygame
from pygame.locals import *
import tkinter as tk
from tkinter import messagebox

clock = pygame.time.Clock()

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
#--------------------------draw grid fuction----------------------------
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

#-------------------------cube object-----------------------------------------
class cube(object):
	"""
	class to create a single grid cube, that has position and movement
	"""
	rows = 20 #set number of rows
	w = 500 #set pixel screen width
	def __init__(self, start, dirnx, dirny, color = WHITE):
		self.pos = start	#touple (x,y)
		self.dirnx = 0
		self.dirny = 0
		self.color = color	#touple(r,g,b)

	def set_direction(self,dirnx,dirny):
		self.dirnx = dirnx
		self.dirny = dirny

	def move(self):
		"""
		move cube, by adding new direction to previous position
		"""
		self.pos = (self.pos[0]+self.dirnx, self.pos[1]+self.dirny)

	def draw(self,surface):
		"""
		drawing: convert x,y grid position to pixel position
		"""
		dis = self.w // self.rows #distance between x and y values
		#variables for easy coding
		i = self.pos[0] # row
		j = self.pos[1] # column
		#draw just a little bit less, so we draw inside of the square. and we dont cover grid.
		pygame.draw.rect(surface, self.color, (i*dis+1,j*dis+1,dis-2,dis-2 ))
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
	def addCube(self):
		"""
		Figure out where is tail, and add a cube after it
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
def redrawWindow(surface):
	global rows, width
	#background
	surface.fill(BLACK)
	#draw grid
	drawGrid(width, rows, surface)
	#draw ball
	ball.draw(surface)
	#update display
	pygame.display.update()
#---------------------------------------------------------------------------------------
def key_events():
	for event in pygame.event.get():
			if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
				#pygame.quit()
				#sys.exit()
				return True

	#in pong we move in only y directions
	keys = pygame.key.get_pressed()
	for key in keys:
		if keys[pygame.K_UP]:
			self.dirny = -1
			self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
		elif keys[pygame.K_DOWN]:
			self.dirny = 1
			self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

	return False
#---------------------------------------------------------------------------------------
def main():
	global width, rows, ball
	#---------------game initialization---------------------------
	#create game display
	width = 500
	rows = 20

	#create game objects
	win = pygame.display.set_mode((width, width)) #square display
	ball = cube((10,1),0,0,WHITE)
	ball.set_direction(1,1) #set initial ball movement direction

	FPScount = 0
	#-----------------------continuous game loop-------------
	GameOver = False
	while not GameOver:
		#pygame.time.delay(50)
		clock.tick(10)	#game max speed 10 FPS
		GameOver = key_events()

		#update ball position
		ball.move()
		#check next direction-------------------------------
		#CONSTRAINTS X
		if ball.pos[0] <= 0 or ball.pos[0] >= rows-1:
			ball.dirnx = -ball.dirnx
		#CONSTRAINTS Y
		if ball.pos[1] <= 0 or ball.pos[1] >= rows-1:
			ball.dirny = -ball.dirny

		#-------------------------------------------------
		#if we are moving in right direction
		#print(f'rows:{rows} ball.pos[0]:{ball.pos[0]} ball.pos[1]:{ball.pos[1]}')
		#FPScount += 1
		#print(FPScount)

		redrawWindow(win)
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
main()
pygame.quit()
sys.exit()
