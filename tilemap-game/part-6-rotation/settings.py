# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 23:08:54 2020

@author: crtom
"""
import pygame as pg

# colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (140, 140, 140)

# game settings
WIDTH = 1024 # divisible by 16*64 32*32
HEIGHT = 768 # 16*48 32*24 66*12

FPS = 60

TITLE = 'Tilemap demo'
BGCOLOR = DARKGREY

TILESIZE = 32

GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

# player settings
# we can say pix/sec, deg/sec only if we use time based movement
PLAYER_ROT_SPEED = 180 # deg/seconds
PLAYER_SPEED = 600 # 100 px/seconds
PLAYER_IMG = 'manBlue_gun.png'
# colision rectange
PLAYER_HIT_RECT =pg.Rect(0, 0, 35, 35)