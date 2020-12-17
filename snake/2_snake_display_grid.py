import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)

class cube(object):
	rows = 0
	w = 0
	def __init__(self,start,dirnx=1,dirny=0,color=(255,0,0)):
		pass

	def move(self,dirnx,dirny):
		pass

	def draw(self,surface,eyes=False):
		pass

class snake(object):
	def __init__(self,color,pos):
		pass

	def move(self):
		pass

	def reset(self,pos):
		pass

	def addCube(self):
		pass

	def draw(self,surface):
		pass

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
	global rows, width
	#background
	surface.fill(BLACK)
	#draw grid
	drawGrid(width, rows, surface)
	#update display
	pygame.display.update()


def randomSnack(rows,items):
	pass

def message_box(subject,content):
	pass

def main():
	global width, rows
	#create game display
	width = 500
	rows = 20
	win = pygame.display.set_mode((width, width)) #square display
	#snake start position
	s = snake(color=RED, pos=(10,10))

	clock = pygame.time.Clock()

	flag = True
	while flag:
		#pygame.time.delay(50)
		clock.tick(10)	#game max speed 10 FPS
		redrawWindow(win)


#rows = 0
#w = 0
#h = 0

#cube.rows = rows
#cube.w = w
print("here")
main()