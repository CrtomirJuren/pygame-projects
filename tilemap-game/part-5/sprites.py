# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 23:13:08 2020

@author: crtom
"""

import pygame as pg
from settings import *

vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
       
        # so player can acces all sprites in the game
        self.game = game
        self.groups = game.all_sprites
        
        # 1.) sprite class default override:
        #Call the parent class (Sprite) constructor
        pg.sprite.Sprite.__init__(self, self.groups)

        # 2.) sprite class default override:
        # tile based game - player is only one tile large
        
        # self.image = pg.Surface((TILESIZE, TILESIZE)) # YELLOW BLOCK SPRITE
        # self.image.fill(YELLOW)
        self.image = game.player_img
        # 3.) sprite class default override:
        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y       
        self.rect = self.image.get_rect()
        
        # CUSTOM ATTRIBUTES
        #self.dt = 0
        self.vel = vec(0, 0)
        self.pos = vec(x, y) * TILESIZE
        self.rot = 0
    
    def get_keys(self):
        self.vel = vec(0, 0)
        self.rot_speed = 0
        
        keys = pg.key.get_pressed()
        
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            # self.player.move(dx=-1)
            self.vel.x = -PLAYER_SPEED
        elif keys[pg.K_RIGHT] or keys[pg.K_d]: # IF ENABLES DIAG
            self.vel.x = PLAYER_SPEED
        if keys[pg.K_UP] or keys[pg.K_w]: # IF ENABLES DIAG
            self.vel.y = -PLAYER_SPEED
        if keys[pg.K_DOWN] or keys[pg.K_s]: # IF ENABLES DIAG
            self.vel.y = PLAYER_SPEED
        
        # DIAGONAL PITAGORA
        if self.vel.x != 0 and self.vel.y != 0:
            self.vel *= 0.7071
    
    def collide_with_walls(self, direction):
        # x collision check
        if direction == 'x':
            hits = pg.sprite.spritecollide(self, self.game.walls, False) # false= dont delete the wall
            
            if hits:
                # sprite was moving to the right
                # we need to put the sprite to the left edge of the wall
                if self.vel.x > 0: 
                    self.pos.x = hits[0].rect.left - self.rect.width
                # sprite was moving to the left
                # we need to put the sprite to the right edge of the wall
                if self.vel.x < 0:
                    self.pos.x = hits[0].rect.right #- self.rect.width    
                
                # we run into the wall, x velocity = 0
                self.vel.x = 0
                # update new position
                self.rect.x = self.pos.x

        if direction == 'y':
            hits = pg.sprite.spritecollide(self, self.game.walls, False) # false= dont delete the wall
            
            if hits:
                # sprite was moving down
                # we need to put the sprite to the top of the wall
                if self.vel.y > 0: 
                    self.pos.y = hits[0].rect.top - self.rect.height
                # sprite was moving to the top
                # we need to put the sprite to the bottom edge of the wall
                if self.vel.y < 0:
                    self.pos.y = hits[0].rect.bottom #- self.rect.width    
                
                # we run into the wall, x velocity = 0
                self.vel.y = 0
                # update new position
                self.rect.y = self.pos.y
                    
    def update(self):
        self.get_keys()

        # this will make movement independant of frame rate
        self.pos += self.vel * self.game.dt # get dt from game object
        
        self.rect.x = self.pos.x
        self.collide_with_walls('x')
        
        self.rect.y = self.pos.y
        self.collide_with_walls('y')
        # check if sprite and a group collides
        # # if hits a wall dont move
        # # redo movement position
        # if pg.sprite.spritecollideany(self, self.game.walls):
        #     self.x -= self.vx * self.game.dt # get dt from game object
        #     self.y -= self.vy * self.game.dt # get dt from game object
        #     # self.rect.x = self.x * TILESIZE
        #     # self.rect.y = self.y * TILESIZE
        #     self.rect.topleft = (self.x, self.y)

class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        
        # so player can acces all sprites in the game
        # member of all sprites group
        # member of all walls group
        self.groups = game.all_sprites, game.walls
        
        pg.sprite.Sprite.__init__(self, self.groups)
        
        self.game = game
        # tile based game - player is only one tile large
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE