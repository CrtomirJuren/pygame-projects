# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 23:12:53 2020

@author: crtom
"""


# KidsCanCode - Game Development with Pygame video series
# Tile-based game - Part 1
# Project setup
# Video link: https://youtu.be/3UxnelT9aCo
from os import path
import pygame as pg
import sys
from settings import *
from sprites import *

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        # this enables keydown repeat instead of clicking
        #Delay is ms after first repeted event. Interval is how fast will repeat happen
        pg.key.set_repeat(50, 50) #set_repeat(delay, interval)
        self.load_data()

    def load_data(self):
        game_folder = path.dirname(__file__)
        file = path.join(game_folder,'map.txt')
            
        self.map_data = []
        with open(file, 'rt') as f:
            for line in f:
                self.map_data.append(line)
                # print(line)
                
    def new(self):
        # initialize all variables and do all the setup for a new game
        # CREATE all sprites group
        self.all_sprites = pg.sprite.Group()
        # CREATE all walls group
        self.walls = pg.sprite.Group()
        # create map and walls here
        # for x in range(10, 20, 1):
        #     Wall(self, x, 5)
        # map_data is 2D
        for row, tiles in enumerate(self.map_data):
            for col, tile in enumerate(tiles):
                # if '1' than create wall
                if tile == '1':
                    Wall(self, col, row)
                # if 'P' set player start position    
                if tile == 'P':
                    # set player start positon
                    self.player = Player(self, col, row) # grid position
                    
    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                pass
                # if key == pg.K_ESCAPE:
            # self.quit()

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

# create the game object
g = Game()
g.show_start_screen()
while True:
    g.new()
    g.run()
    g.show_go_screen()