# -*- coding: utf-8 -*-
"""
http://inventwithpython.com/pygame/

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
WIN_W = 600
WIN_H = 600 
""" grid calculations
 GRID = 600*600
 GRID 6x6 = 36 pieces
 100x100 per square
 one piece is 80x80 + margin = 100x100
"""
MARGIN_L = 10
BOX_L = 80

#REVEALSPEED = 8

#GAPSIZE = 10
BOARD_W = 6
BOARD_H = 6

# check
#assert(BOARDWIDTH*BOARDHEIGHT) % 2 == 0, 'Board needs to have an even number of boxes for pairs of matches'

#XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH * (BOXSIZE + GAPSIZE))) / 2)
#YMARGIN = int((WINDOWHEIGHT - (BOARDHEIGHT * (BOXSIZE + GAPSIZE))) / 2)

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

LINE = 'line'
DONUT = 'donut'
SQUARE = 'square'
DIAMOND = 'diamond' 
LINES = 'lines'
OVAL = 'oval'


#ALLCOLORS = (RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN)
#ALLSHAPES = (LINE, DONUT, SQUARE, DIAMOND, LINES, OVAL)

#assert len(ALLCOLORS) * len(ALLSHAPES) * 2 <= BOARDWIDTH * BOARDHEIGHT,'Board is too big for the number of shapes/colors defined.'

# create coordiantion
grid_vertices = 0

grid_vertices = [[0 for i in range(6)] for j in range(6)]

# create a list of touple positions
grid_touple_lst = []
for y in range(0, 6):
    for x in range(0, 6):
        grid_touple_lst.append((x,y))
    

print(grid_touple_lst)
# print('first item:', grid_touple_lst[0])
# print('last item:', grid_touple_lst[35])

square_touple_lst = []
for x in range(10, 610, 100):
    for y in range(10, 610, 100):
        square_touple_lst.append((x,y))
# print(square_touple_lst)

# 'back'
# 'front'    
state_lst = ['back' for i in range(36)]
print(state_lst)

#------------------------------------------------------------------------------
#----------------------------main loop-----------------------------------------
#------------------------------------------------------------------------------
def main():
    
    # global variables
    global FPSCLOCK, DISPLAYSURF
    
    # for positions
    position_pixel = (None, None)
    position_grid = (None, None)
    position_box = None
    
    # for user events
    mouseMoved = False
    mouseClicked = False
    
    #--------------------------------------------------------------------------
    # init pygame
    pygame.init()
    
    FPSCLOCK = pygame.time.Clock() # initialize clock
    
    DISPLAYSURF = pygame.display.set_mode((WIN_W, WIN_H)) # initialize surface
    DISPLAYSURF.fill(BGCOLOR)
    
    pygame.display.set_caption('Memory Game')

    # Draws boxes being covered/revealed. "boxes" is a list
    # of two-item lists, which have the x & y spot of the box.
    # coordinartes of grid
    
    #left, top = leftTopCoordsOfBox(box[0], box[1])
    #pygame.draw.rect(DISPLAYSURF, BGCOLOR, (left, top, BOXSIZE, BOXSIZE))
    # DRAW GRID
    for touple in square_touple_lst:
        x, y = touple
        pygame.draw.rect(DISPLAYSURF, WHITE, (x, y, 80, 80))

    
    #shape, color = getShapeAndColor(board, box[0], box[1])
    #drawIcon(shape, color, box[0], box[1])

    
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
                position_pixel = event.pos
                mouseMoved = True
                #print('mouse moved')

            elif event.type == MOUSEBUTTONUP:
                # mouse click position is in pixels
                position_pixel = event.pos
                # set click is true for functions
                mouseCicked = True
                #print('mouse clicked')
        #---------------------------------------------------------------------
        # if mouse moved than highlight box
        if mouseMoved:
            # window pixels to game grid 
            position_grid = pixel_pos_to_game_grid(position_pixel)
            # game grid to box number
            position_box = game_grid_to_touple_pos(position_grid)
            
            print('position_pixel = ', position_pixel)
            print('position_grid = ', position_grid)
            print('position_box = ', position_box)
              
            # reset event flag
            mouseMoved = False
        #---------------------------------------------------------------------
        if mouseClicked:
            mouseClicked = False
        #------------------------timing----------------------------------------
        # draws surface object stored in DISPLAYSURF
        pygame.display.update()
        FPSCLOCK.tick(FPS)
    
#------------------------------------------------------------------------------
#-------------------------function definitions---------------------------------
#------------------------------------------------------------------------------
def pixel_pos_to_game_grid(touple_pixel):
    """
    Parameters
    ----------
    touple_pixel : touple
        position in pixels coordinates.

    Returns
    -------
    touple_grid : touple
        position in game grid coordinates.
    """

    x_grid = touple_pixel[0] // 100 # integere division
    y_grid = touple_pixel[1] // 100
    touple_grid = (x_grid, y_grid)

    return touple_grid

def game_grid_to_touple_pos(touple_grid):
    """
    Parameters
    ----------
    mytouple : touple
        position in game grid coordinates.

    Returns
    -------
    box_n : number
        list index from grid_touple_lst
    """

    box_n = None
    for i, touple in enumerate(grid_touple_lst):
        if touple_grid == touple:
            box_n = i
    
    return box_n

    

def change_box_state(grid_nx, grid_ny):
    global state_lst
    
    
    
    # for state in state_lst:
    #     # if back, turn to front
    #     if state == 'front':
    #         pygame.draw.rect(DISPLAYSURF, WHITE, (x, y, 80, 80))
    #     # if front, turn to back
    #     else:
    #         pygame.draw.rect(DISPLAYSURF, RED, (x, y, 80, 80))



def leftTopCoordsOfBox(boxx, boxy):
    # Convert board coordinates to pixel coordinates
    left = boxx * (BOXSIZE + GAPSIZE) + XMARGIN
    top = boxy * (BOXSIZE + GAPSIZE) + YMARGIN
    return (left, top)    
#------------------------------------------------------------------------------
#-------------------------Start application------------------------------------
#------------------------------------------------------------------------------        
if __name__ == '__main__':
    main()