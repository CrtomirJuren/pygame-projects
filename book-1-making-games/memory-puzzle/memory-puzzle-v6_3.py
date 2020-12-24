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
import random

from pygame.locals import * # this is for shortcut pygame.QUIT -> QUIT

import time

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
GREY    = (128, 128, 128)
SILVER  = (192, 192, 192)

RED     = (255,   0,   0)
YELLOW  = (255, 255,   0)
ORANGE  = (255, 128,   0)
MAGENTA = (255,   0, 255)
PURPLE  = (128,   0, 128)

LIME    = (  0, 255,   0)
BLUE    = (  0,   0, 255)
NAVYBLUE= ( 60,  60, 100)
CYAN    = (  0, 255, 255)
GRAY	= (128, 128, 128)
MAROON  = (128,   0,   0)
OLIVE   = (128, 128,   0)
GREEN   = (  0, 128,   0)
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

#------------------CREATE GAME GRID------------------------

# create a list of touple positions
grid_touple_list = []
grid_pixel_pos_list = []
grid_card_pos_list = []

for y in range(0, 6):
    for x in range(0, 6):
        grid_touple_list.append((x,y))
        grid_pixel_pos_list.append((x*100, y*100))
        grid_card_pos_list.append(((x*100) + 10, (y*100) + 10))

#---------------ICONS------------------------

def create_icon(shape, color):
    icon_surface = pygame.Surface((50, 50))
    
    #----------square filled----------------
    if shape == 'square_filled':
        pygame.draw.rect(icon_surface, color, [10,10,30,30])
    
    elif shape == 'square_empty':
        pygame.draw.rect(icon_surface, color, [10,10,30,30],5)    
    
    elif shape == 'circle_filled':
        pygame.draw.circle(icon_surface, color, (25, 25 ), 15)
   
    elif shape == 'circle_empty':
        pygame.draw.circle(icon_surface, color, (25, 25 ), 15, 5)
    
    elif shape == 'triangle_filled':
        pygame.draw.polygon(icon_surface, color, ((10,40),(40,40),(25, 10)))
    
    elif shape == 'triangle_empty':
        pygame.draw.polygon(icon_surface, color, ((10,40),(40,40),(25, 10)),4)
    
    return icon_surface

icon_shapes = ['square_filled',
               'square_empty',
               'circle_filled',
               'circle_empty',
               'triangle_filled',
               'triangle_empty']

# 36 CARDS = 12 icon pairs * 3 colours
icon_shapes = 2 * icon_shapes # create pairs of shapes = 6 pairs -> 12 cards
icon_colors = [RED, GREEN, BLUE]

#icon = {'surface': surface,'shape': shape,'color': color}
icons = []
for color in icon_colors:
    for shape in icon_shapes:
        surface = create_icon(shape, color)
        icons.append({'surface': surface,'shape': shape,'color': color})
#print(icons)

# shuffle icon list
random.seed(99)
random.shuffle(icons)


#----------card-----------
# 36 tiles
cards = []
for i in range(36):
    
    # initialize with closed and not highlighted
    state = 'closed' #opened
    glow = False # True
    solved = False
    
    # each card is positioned on game grid
    position = grid_card_pos_list[i]
    rectangle = [position[0], position[1], 80, 80]
    
    #each card has its own surface
    surface = pygame.Surface((80,80))
    
    # each card has its own surface icon
    icon_surface = icons[i]['surface']
    icon_color = icons[i]['color']
    icon_shape = icons[i]['shape']
    
    card = {'card_n': i,
            'position': position,
            'surface': surface,
            'rectangle': rectangle,
            'glow': glow,
            'state': state,
            'solved': solved,
            'icon_surface': icon_surface,
            'icon_color': icon_color,
            'icon_shape': icon_shape}

    cards.append(card)
# print(cards)
#------------------------------------------------------------------------------
#----------------------------main loop-----------------------------------------
#------------------------------------------------------------------------------
def main():

    # global variables
    global FPSCLOCK, DISPLAYSURF, cards

    # for game logic state
    state = 0
    # 0 = idle
    # 1 = first card opened
    # 2 = second card opened
    # 
    state_transition = True
    # for positions
    position_pixel = (None, None)
    position_grid = (None, None)
    position_box = None
    position_box_old = None

    # for user events
    mouseMoved = False
    mouseClicked = False
    cardSelected = False
    
    card_pair = []
    
    #--------------------------------------------------------------------------
    # init pygame
    pygame.init()

    FPSCLOCK = pygame.time.Clock() # initialize clock
    DISPLAYSURF = pygame.display.set_mode((WIN_W, WIN_H)) # initialize surface
    pygame.display.set_caption('Memory Game')

    draw_background()

    update_cards()

    #--------------------------------------------------------------------------
    #-------------------------GAME loop----------------------------------------
    #--------------------------------------------------------------------------
    gameOver = False
    while not gameOver:

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
                mouseClicked = True
                #print('mouse clicked')
                
            #---------------------------------------------------------------------
            # if mouse moved than highlight box
            if mouseMoved:
                # reset event flag
                mouseMoved = False
                # window pixels to game grid
                position_grid = pixel_pos_to_game_grid(position_pixel)
                # game grid to box number
                position_box = game_grid_to_touple_pos(position_grid)
    
                # print('position_pixel = ', position_pixel)
                # print('position_grid = ', position_grid)
                #print('position_box = ', position_box)
    
                glow_card(position_box)
      
    
            #---------------------------------------------------------------------
            elif mouseClicked: #and cardSelected
                # reset event flag
                mouseClicked = False
                print('mouse clicked')
                
                # # get clicked card properties
                card = cards[position_box]
                
                # # only do stuff on closed cards
                if card['state'] == 'closed': 
                    print('closed card selected')
                    
                #     # check if new card selected
                #     if  position_box !=  position_box_old:
                #         position_box_old = position_box
                #         print('new card opened')
                
                    state += 1
                    state_transition = True
                    
        #--------------------------GAME STATEMACHINE----------------------------            
        if state == 0:
            if state_transition:
                print('state 0: waiting on first card to open')
                state_transition = False
        
        # SHOW FIRST SELECTED CARD
        elif state == 1:
            print('state 1: first card opened')

            open_card(position_box)
            card_0 = position_box
            state = 2
        
        elif state == 2:
            if state_transition:
                print('state 2: waiting on second card to open')
                state_transition = False
            
        # SHOW SECOND SELECTED CARD    
        elif state == 3:
            print('state 3: second card opened')

            open_card(position_box)
            card_1 = position_box

            state = 4

        # AUTOMATIC: CHECK IF CARDS ARE PAIR   
        elif state == 4:        
            print('state 4: checking for conditions')       
            time.sleep(1)
            state = 0

            shapeMatch = False
            colorMatch = False
            
            if cards[card_0]['icon_color'] == cards[card_1]['icon_color']:
                colorMatch = True
            if cards[card_0]['icon_shape'] == cards[card_1]['icon_shape']:
                shapeMatch = True
            
            if colorMatch and shapeMatch:
                cards[card_0]['solved'] = True
                cards[card_1]['solved'] = True
                print('its a pair!')
            else:
                cards[card_0]['state'] = 'closed'
                cards[card_1]['state'] = 'closed'
                print('no pair')            
            
            update_cards()
            
            # CHECK IF ALL CARDS ARE SOLVED
            solved = []
            for card in cards:
                solved.append(card['solved'])
                
            #All checks wether all values in a list interpret to True
            if all(solved):
                print('congratulations, all cards solved, you have won !')
                time.sleep(2)
                gameOver = True

        #------------------------timing----------------------------------------
        # draws surface object stored in DISPLAYSURF
        pygame.display.flip()
        FPSCLOCK.tick(FPS)

#------------------------------------------------------------------------------
#-------------------------function definitions---------------------------------
#------------------------------------------------------------------------------
def update_cards():
    global cards

    for card in cards:

        if card['state'] == 'opened':
            #pygame.draw.circle(DISPLAYSURF, RED, (card['rectangle'][0], card['rectangle'][1]), 2)
            #surface.blit(DISPLAYSURF, card['rectangle'])
            card['surface'].blit(card['icon_surface'], (15, 15))
        else:
            #card['surface'].blit(card['icon_surface'], (15, 15))
            card['surface'].fill(BLACK)

    # blit all cards to DISPLAYSURF
    for card in cards:
        DISPLAYSURF.blit(card['surface'], card['rectangle'])



def open_card(position_box):
    global cards

    cards[position_box]['state'] = 'opened'    
        
    # blit all cards to DISPLAYSURF
    for card in cards:
        if card['state'] == 'opened':
            card['surface'].blit(card['icon_surface'], (15, 15))
        else:
            card['surface'].fill(BLACK)

        DISPLAYSURF.blit(card['surface'], card['rectangle'])

def glow_card(position_box):
    global cards

    for i, card in enumerate(cards):
        # set highlight selected card
        if i == position_box:
            cards[i]['glow'] = True
        else:
            cards[i]['glow'] = False
    
    for card in cards:
        # if card is selected, glow sides
        if card['glow']:
            # draw smaller rectangle for glowing
            glow_pos = [card['rectangle'][0]+2,
                        card['rectangle'][1]+2,
                        card['rectangle'][2]-4,
                        card['rectangle'][3]-4]
            pygame.draw.rect(card['surface'], BLUE, [0,0,78,78], 4)
        else:
            pygame.draw.rect(card['surface'], BLACK, [0,0,78,78], 4)
        
        # blit every card surface on DISPLAYSURF
        DISPLAYSURF.blit(card['surface'], card['rectangle'])
    
#--------------------------BACKGROUND--------------------------------------
def draw_background():
    background = pygame.Surface(DISPLAYSURF.get_size())
    ts, w, h, c1, c2 = 100, *DISPLAYSURF.get_size(), (160, 160, 160), (192, 192, 192)
    tiles = [((x*ts, y*ts, ts, ts), c1 if (x+y) % 2 == 0 else c2) for x in range((w+ts-1)//ts) for y in range((h+ts-1)//ts)]

    for rect, color in tiles:
        pygame.draw.rect(background, color, rect)

    DISPLAYSURF.blit(background, (0, 0))
    
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
    position_box : number
        list index from grid_touple_lst
    """

    box_n = None
    for i, touple in enumerate(grid_touple_list):
        if touple_grid == touple:
            position_box = i

    return position_box

#------------------------------------------------------------------------------
#-------------------------Start application------------------------------------
#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
    
    pygame.quit()
    sys.exit()