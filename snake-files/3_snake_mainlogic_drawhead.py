"""Snake Game Python Tutorial
youtube video: https://www.youtube.com/watch?v=CD4qAhfFuLo
current time: 26:00
"""
import sys
import math
import random
import pygame
from pygame.locals import *
import tkinter as tk
from tkinter import messagebox

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)

class cube(object):
	"""
	"""
	rows = 20 #set number of rows
	w = 500 #set pixel screen width
	def __init__(self,start,dirnx=1,dirny=0,color=RED):
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
		self.pos(self.pos[0]+self.dirnx, self.pos[1]+self.dirny)

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
			for keys in keys:
				if keys[pygame.K_LEFT]:
					self.dirnx = -1
					self.dirnx = 0
					# we mustremember where we turned, so other cubes can follow
					# add a new key
					#example - here we turned in thar way
					self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
				elif keys[pygame.K_RIGHT]:
					self.dirnx = 1
					self.dirnx = 0
					self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
				elif keys[pygame.K_UP]:
					self.dirnx = 0
					self.dirnx = -1
					self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
				elif keys[pygame.K_DOWN]:
					self.dirnx = 0
					self.dirnx = 1
					self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

		#look trough all position of snake
		#we get the index=i and the cube=c of body
		for index, cube in enumerate(self.body):
			position = cube.pos[:]
			#for each of the sube, we grab position and check turn
			#if this position in turns, than we move
			if position in self.turns:
				turn = self.turns[position]
				#here we store direction where to move
				cube.move(turn[0],turn[1])
				#if we are on the last cube of the snake, remove the turn, we finished it
				if index == len(self.body)-1:
					self.turns.pop(position)

			else:	#CHECK IF WE REACHED EDGE OF THE SCREEN
				#if MOVE LEFT & we are at the left side of screen
				if (cube.dirnx == -1) and (cube.position[0] <= 0):
					cube.position = (cube.rows-1,cube.position[1])
				#if MOVE RIGHT & we are at the left side of screen
				if (cube.dirnx == 1) and (cube.position[0] >= cube.rows-1):
					cube.position = (0,cube.position[1])
				#if MOVE DOWN & we are at the left side of screen
				if (cube.dirny == 1) and (cube.position[1] >= cube.rows-1):
					cube.position = (cube.position[1],0)
				#if MOVE UP & we are at the left side of screen
				if (cube.dirny == -1) and (cube.position[1] <= 0):
					cube.position = (cube.position[0],0)
				#normal move of cube
				else:
					cube.move(cube.dirnx,cube.dirny)

	def reset(self,pos):
		pass

	def addCube(self):
		pass

	def draw(self,surface):
		for index, cube in enumerate(self.body):
			#check where to draw eyes for snake head
			if index == 0:
				cube.draw(surface,True) #with eyes
			else:
				cube.draw(surface,False) #without eyes


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

def redrawWindow(surface):
	global rows, width, s
	#background
	surface.fill(BLACK)
	s.draw(surface)
	#draw grid
	drawGrid(width, rows, surface)
	#update display
	pygame.display.update()

def randomSnack(rows,items):
	pass

def message_box(subject,content):
	pass

def key_events():
	pass

#directions = {"right":(1,0), "left":(0,-1), "up":(0,-1), "down":(0,1)}

def main():
	global width, rows, s
	#create game display
	width = 500
	rows = 20
	win = pygame.display.set_mode((width, width)) #square display
	#snake start position
	s = snake(color=RED, pos=(10,10))

	clock = pygame.time.Clock()

	flag = True
	count = 0
	print(count)
	while flag:
		#pygame.time.delay(50)
		clock.tick(10)	#game max speed 10 FPS
		redrawWindow(win)
		count += 1
		print(count)

#rows = 0
#w = 0
#h = 0

#cube.rows = rows
#cube.w = w
main()
pygame.quit()
sys.exit()