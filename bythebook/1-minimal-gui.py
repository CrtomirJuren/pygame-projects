# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 18:09:41 2020

@author: crtom
"""

import pygame
import sys

from pygame.locals import * # this is for shortcut pygame.QUIT -> QUIT

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
    
    # draws surface object stored in DISPLAYSURF
    pygame.display.update()

    pygame.time.wait(100)