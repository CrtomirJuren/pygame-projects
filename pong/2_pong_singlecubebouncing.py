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
