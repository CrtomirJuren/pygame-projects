# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 18:09:41 2020

@author: crtom

- BASIC ARHITECTURE, get mouse coordinates

#------------------------------------------------------------------------------
    #--------------------------------------------------------------------------
        #----------------------------------------------------------------------
            #------------------------------------------------------------------
                #--------------------------------------------------------------
"""

import pygame
import sys

from pygame.locals import * # this is for shortcut pygame.QUIT -> QUIT

#--------------------------------------------------------------------------
#-------------------------constants----------------------------------------
#--------------------------------------------------------------------------

FPS = 30
WINDOWWIDTH = 640 
WINDOWHEIGHT = 480 
REVEALSPEED = 8
BOXSIZE = 40
GAPSIZE = 10
BOARDWIDTH = 10
BOARDHEIGHT = 7

# check
assert(BOARDWIDTH*BOARDHEIGHT) % 2 == 0, 'Board needs to have an even number of boxes for pairs of matches'

XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH * (BOXSIZE + GAPSIZE))) / 2)
YMARGIN = int((WINDOWHEIGHT - (BOARDHEIGHT * (BOXSIZE + GAPSIZE))) / 2)

# COLORS  ( R ,  G ,  B )
WHITE   = (255, 255, 255)
BLACK   = (  0,   0,   0)
RED     = (255,   0,   0)
LIME    = (  0, 255,   0)
BLUE    = (  0,   0, 255)
NAVYBLUE= ( 60,  60, 100)
YELLOW  = (255, 255,   0)
ORANGE  = (255, 128,   0)
CYAN    = (  0, 255, 255)
MAGENTA = (255,   0, 255)
SILVER  = (192, 192, 192)
GRAY	= (128, 128, 128)
MAROON  = (128,   0,   0)
OLIVE   = (128, 128,   0)
GREEN   = (  0, 128,   0)
PURPLE  = (128,   0, 128)
TEAL    = (  0, 128, 128)
NAVY    = (  0,   0, 128)

BGCOLOR = NAVYBLUE
LIGHTBGCOLOR = GRAY
BOXCOLOR = WHITE
HIGHLIGHTCOLOR = BLUE

DONUT = 'donut'
SQUARE = 'square'
DIAMOND = 'diamond' 
LINES = 'lines'
OVAL = 'oval'

ALLCOLORS = (RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN)
ALLSHAPES = (DONUT, SQUARE, DIAMOND, LINES, OVAL)

assert len(ALLCOLORS) * len(ALLSHAPES) * 2 <= BOARDWIDTH * BOARDHEIGHT,'Board is too big for the number of shapes/colors defined.'

#------------------------------------------------------------------------------
#----------------------------main loop-----------------------------------------
#------------------------------------------------------------------------------
def main():
    
    # global variables
    global FPSCLOCK, DISPLAYSURF
    
    # for mouse pos
    mousex = 0
    mousey = 0
    
    #--------------------------------------------------------------------------
    # init pygame
    pygame.init()
    
    FPSCLOCK = pygame.time.Clock() # initialize clock
    
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT)) # initialize surface
    DISPLAYSURF.fill(BGCOLOR)
    
    pygame.display.set_caption('Memory Game')

    #--------------------------------------------------------------------------
    #-------------------------GAME loop----------------------------------------
    #--------------------------------------------------------------------------
    while True:
        
        #----------------------event handling---------------------------------
        for event in pygame.event.get():
            
            # event objects have type attribute
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseCicked = True
                print(mousex, mousey)
        
        #------------------------timing----------------------------------------
        # draws surface object stored in DISPLAYSURF
        pygame.display.update()
        FPSCLOCK.tick(FPS)
    
#------------------------------------------------------------------------------
#-------------------------function definitions---------------------------------
#------------------------------------------------------------------------------
    
#------------------------------------------------------------------------------
#-------------------------Start application------------------------------------
#------------------------------------------------------------------------------        
if __name__ == '__main__':
    main()