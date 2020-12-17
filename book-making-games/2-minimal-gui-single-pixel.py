# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 18:09:41 2020

@author: crtom
"""

import pygame
import sys

from pygame.locals import * # this is for shortcut pygame.QUIT -> QUIT

def drawPoint(x,y,color):

    s = pygame.Surface((1,1))   # the object surface 1 x 1 pixel (a point!)

    s.fill(color)               # color as (r,g,b); e.g. (100,20,30)

    # now get an object 'rectangle' from the object surface and place it at position x,y

    r,r.x,r.y = s.get_rect(),x,y    

    screen.blit(s,r)            # link the object rectangle to the object surface

pygame.init()

# returns pygame.Surface objet for window
DISPLAYSURF = pygame.display.set_mode((400,300))

pygame.display.set_caption('Hello World!')

while True:
    
    # event handling
    for event in pygame.event.get():
        
        # event objects have type attribute
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    
    #drawPoint(1, 1, (0,0,0))
    #window_surface.set_at((x, y), my_color)
    DISPLAYSURF.set_at((100, 100), (255,255,0))
    # draws surface object stored in DISPLAYSURF
    pygame.display.update()

    pygame.time.wait(100)