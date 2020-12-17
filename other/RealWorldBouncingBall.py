"""
Python: Bouncing Ball Animation with Real-World Physics!!
video: https://www.youtube.com/watch?v=9LWpCtbSvG4

Analyst Rising 1.36K subscribers

In this tutorial I will be showing you how to code/programme
a bouncing ball, with REAL-WORLD PHYSICS, in Python.
This is one of many great python tutorials that should
get you well on your way to programming some amazing stuff!!
"""

import pygame
from pygame.locals import *
import time

pygame.init()
#---------game constants variables-------------
display_width = 300
display_height = 400
#RGB color constants
black = (0,0,0)
white = (255,255,255)
red   = (255,0,0)
green = (0,255,0)
blue  = (0,0,255)

update_ms = 100
frame_speed_sec = (1/update_ms)*1000

#------------------------------------------------------
#create main display window
gameDisplay = pygame.display.set_mode((display_width,display_height))
#set main display window title
pygame.display.set_caption('gameDisplay')

clock = pygame.time.Clock()

#----------------------FUNCTIONS-------------------------
def fps_display_counter(count):
	#1. set type font
	font = pygame.font.SysFont(None,25)
	#2. render it
	text = font.render("FPS count: " + str(count),True,white)
	#3. blit = draw
	gameDisplay.blit(text,(0,0))

class Particle(object):
	def __init__(self, x, y, size, colour, thickness):
	    self.x = x
	    self.y = y
	    self.size = size
	    self.colour = colour
	    self.thickness = thickness

	def display(self):
		#pygame.draw.
		pygame.draw.circle(gameDisplay, self.colour, (self.x, self.y), self.size, self.thickness)

def game_loop(frame_speed):
	#main game loop
	run = True
	counter = 0
	velocity_x = 10
	velocity_y = -10
	gravity = 0.7
	friction = 0.5

	while run:
		counter += 1
		#-----------check for pressed keys----------------
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
				run = False
		#-------------------------------------------------

		#CONSTRAINTS X
		if particle.x - particle.size <= 0 or particle.size + particle.x >= display_width:
			velocity_x = -velocity_x
		
		#CONSTRAINTS Y
		if particle.y - particle.size <= 0 or particle.size + particle.y >= display_height:
			velocity_y = -velocity_y

		particle.x += velocity_x
		particle.y += velocity_y
		#-------------------------------------------------
		gameDisplay.fill(black) # draw background
		fps_display_counter(counter)
		particle.display()			#draw particle ball
		pygame.display.update()		#update display
		clock.tick(frame_speed)	#set FPS update frequency


#---------------------------------------
#-----------initialization--------------
particle = Particle(x=150, y=50, size=10, colour=white, thickness=0)

#-------------main loop-----------------
game_loop(frame_speed_sec)
#---------------------------------------
#---------------------------------------