"""
Animation Spritesheet
- picture size 32*640
- 10 pictures
- 2 rows by 5 pictures

Main goal:
- cutting subpictures out of a single spritesheet image
#-------------------------------------------------
picture idexes
0, 1, 2, 3, 4,
5, 6, 7, 8, 9,

picture column, row position
(0,0) (1,0) (2,0) (3,0) (4,0)
(0,1) (1,1) (2,1) (3,1) (4,1)

picture column, row pixel position
(0,0) (32,0) (64,0) (96,0) (128,0)
(0,32) (32,32) (64,32) (96,32) (128,32)
#--------------------------------------------------
HANDLES = are used for easy picture offsets
     	-
    8 	7   6
     	-
  --5---4---3---
	 	-
	2 	1   0
	 	-

index offset
  0	  (0,0)
  1	  (-hw,0)
  2   (-w,0)
  3   (0,-hh)
  4   (-hw,-hh)	#image is centralized
  5   (-w,-hh)
  6   (0,-h)
  7   (-hw,-h)
  8   (w,-h)
"""

import math,random,sys
import pygame
from pygame.locals import *

#esit the program
def events():
	for event in pygame.event.get():
		if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
			pygame.quit()
			sys.exit()

#define display surface
W,H = 320,320
HW, HH = W//2, H//2
AREA = W*H

#initialize display
pygame.init()
CLOCK = pygame.time.Clock()
DS = pygame.display.set_mode((W,H))
pygame.display.set_caption("sprite sheets")
FPS = 1

#define colours
BLACK = (0,0,0)
WHITE = (255,255,255)
background = pygame.image.load('background.png').convert_alpha()
#--------------------------------------

class spritesheet:
	def __init__(self, filename,cols,rows):
		self.sheet = pygame.image.load(filename).convert_alpha()

		self.cols =cols
		self.rows = rows
		self.totalCellCount = cols*rows
		#print(f'self.totalCellCount {self.totalCellCount}') OK

		self.rect = self.sheet.get_rect()	#calling this function gives use rect width
		#cell width
		w = self.cellWidth = self.rect.width // cols
		h = self.cellHeight = self.rect.height // rows
		hw,hh = self.cellCenter = (w//2,h//2)

		#print(f'self.rect.width{self.rect.width} self.rect.height:{self.rect.height}') OK

		#print(f'w={w}, h={h}')
		#print(f'hw={hw}, hh={hh}')

		#build a list of cells. We need every cell x and y in pixels
		#1.) build list of indexes and than multiply those indexes by pixel size
		self.cells = list([(index%cols*w,index//cols*h,w,h) for index in range(self.totalCellCount)])
		self.handle = list([(0,0),(-hw,0),(-w,0),(0,-hh),(-hw,-hh),(-w,-hh),(0,-h),(-hw,-h),(w,-h)])

	def draw(self, surface, cellIndex, x, y, handle):
		surface.blit(self.sheet,(x+self.handle[handle][0],y+self.handle[handle][1]),self.cells[cellIndex])

	#----------------------------------------
s = spritesheet(filename="moon_phase_64x320_v1.png",cols=10,rows=2)
CENTER_HANDLE = 4
index = 0

#main loop
print (s.handle)
while True:
	events()
	#draw spritesheet
	#DS.fill(BLACK)
	DS.blit(background, (0,0))
	s.draw(DS, index% s.totalCellCount, HW//2,HH//2,CENTER_HANDLE)
	index += 1
	pygame.draw.circle(DS,WHITE,(HW,HH),2,0)
	pygame.display.update()
	CLOCK.tick(FPS)
	DS.fill(WHITE)
