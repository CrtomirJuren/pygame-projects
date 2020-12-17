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
#---------------------------------------------------------------------------------------
def key_events():
	for event in pygame.event.get():
			if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
				#pygame.quit()
				#sys.exit()
				return True

	keys = pygame.key.get_pressed()
	for key in keys:
		if keys[pygame.K_UP]:
			self.dirnx = 0
			self.dirny = -1
			self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
		elif keys[pygame.K_DOWN]:
			self.dirnx = 0
			self.dirny = 1
			self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

	return False
#---------------------------------------------------------------------------------------
def main():
	global width, rows, s, snack
	#---------------game initialization---------------------------
	#create game display
	width = 500
	rows = 20
	win = pygame.display.set_mode((width, width)) #square display

	clock = pygame.time.Clock()

	FPScount = 0
	#-----------------------continuous game loop-------------
	GameOver = False
	while not GameOver:
		#pygame.time.delay(50)
		clock.tick(10)	#game max speed 10 FPS
		GameOver = key_events()


		print(FPScount)

		redrawWindow(win)
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
main()
pygame.quit()
sys.exit()