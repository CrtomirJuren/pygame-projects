# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 18:09:41 2020

@author: crtom
"""

import pygame
import sys
#from vector2 import Vector2
#from vector2 import *

from gameobjects.vector2 import *
from pygame.locals import * # this is for shortcut pygame.QUIT -> QUIT

# for antialiased
from pygame import gfxdraw

def draw_circle(surface, x, y, radius, color):
    gfxdraw.aacircle(surface, x, y, radius, color)
    gfxdraw.filled_circle(surface, x, y, radius, color)
    
pygame.init()

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()


# returns pygame.Surface objet for window
DISPLAYSURF = pygame.display.set_mode((400,400))

pygame.display.set_caption('Hello World!')

#point A
A = (10.0, 10.0)
#point B
B = (300.0, 300.0)

# vector of distance between points AB
AB = Vector2.from_points(A, B)

# step vector, length of 1/10 AB
step = AB * .01

#start position vector at point A
position = Vector2(A[0], A[1])

# for n in range(10):
#     position += step
#     print(position)

#create point
#pygame.draw.circle(screen, self.colour, (self.x, self.y), self.size, self.thickness)

Running = True
while Running:
    
    # event handling
    for event in pygame.event.get():
        
        # event objects have type attribute
        if event.type == QUIT:
            Running = False
    
    position += step
    #print(position.x)
    
    # clear background
    DISPLAYSURF.fill((0,0,0))
    
    pygame.draw.line(DISPLAYSURF, (255, 255, 255),(A[0],A[1]),(position.x, position.y))
    #pygame.draw.circle(DISPLAYSURF, (255,255,255), (int(position.x), int(position.y)), 5, 0)    
    draw_circle(DISPLAYSURF, int(position.x), int(position.y), 5, (255,255,255))
    
    # check when vector reaches position
    if position.x >= AB.x and position.y >= AB.y:
        print('reached pos')
        Running = False
        
    # draws surface object stored in DISPLAYSURF
    pygame.display.update()
    
    #pygame.time.wait(100)
    fpsClock.tick(FPS)

pygame.quit()
sys.exit()