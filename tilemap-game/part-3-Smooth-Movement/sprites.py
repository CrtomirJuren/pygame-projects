# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 23:13:08 2020

@author: crtom
"""

import pygame as pg
from settings import *

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
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(YELLOW)
        
        # 3.) sprite class default override:
        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y       
        self.rect = self.image.get_rect()
        #self.rect.center = (WIDTH // 2, HEIGHT // 2)
        
        # CUSTOM ATTRIBUTES
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        # delta time, game loop time
        #self.dt = 0
        self.vx, self.vy = 0, 0

        # position vector
        #self.position =  Vector2(100.0, 100.0)
        # direction vector
        #self.direction = Vector2(0, 0)  
        # movement speed
        #self.speed = 300.        
    
    def get_keys(self):
        self.vx, self.vy = 0, 0
        
        keys = pg.key.get_pressed()
        
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            # self.player.move(dx=-1)
            self.vx = -PLAYER_SPEED
        elif keys[pg.K_RIGHT] or keys[pg.K_d]: # IF ENABLES DIAG
            self.vx = PLAYER_SPEED
        if keys[pg.K_UP] or keys[pg.K_w]: # IF ENABLES DIAG
            self.vy = -PLAYER_SPEED
        if keys[pg.K_DOWN] or keys[pg.K_s]: # IF ENABLES DIAG
            self.vy = PLAYER_SPEED
        
        # DIAGONAL PITAGORA
        if self.vx != 0 and self.vy != 0:
            self.vx *= 0.7071
            self.vy *= 0.7071
    
    #def set_time_passed_sec(self, dt):
    #    self.dt_sec = dt / 1000.0
    # def move(self, dx=0, dy=0):
    #     # only move if not colliding with walls
    #     if not self.collide_with_walls(dx, dy):
    #         self.x += dx
    #         self.y += dy
    
    # def collide_with_walls(self, dx = 0, dy = 0):
    #     # OLD collision check
    #     # loop trough the wall group and check
    #     for wall in self.game.walls:
    #         if wall.x == self.x + dx and wall.y == self.y + dy:
    #             # yes we did collide
    #             return True
    #     #no we didnt collide with wall
    #     return False
    def collide_with_walls(self, direction):
        # x collision check
        if direction == 'x':
            hits = pg.sprite.spritecollide(self, self.game.walls, False) # false= dont delete the wall
            
            if hits:
                # sprite was moving to the right
                # we need to put the sprite to the left edge of the wall
                if self.vx > 0: 
                    self.x = hits[0].rect.left - self.rect.width
                # sprite was moving to the left
                # we need to put the sprite to the right edge of the wall
                if self.vx < 0:
                    self.x = hits[0].rect.right #- self.rect.width    
                
                # we run into the wall, x velocity = 0
                self.vx = 0
                # update new position
                self.rect.x = self.x

        if direction == 'y':
            hits = pg.sprite.spritecollide(self, self.game.walls, False) # false= dont delete the wall
            
            if hits:
                # sprite was moving down
                # we need to put the sprite to the top of the wall
                if self.vy > 0: 
                    self.y = hits[0].rect.top - self.rect.height
                # sprite was moving to the top
                # we need to put the sprite to the bottom edge of the wall
                if self.vy < 0:
                    self.y = hits[0].rect.bottom #- self.rect.width    
                
                # we run into the wall, x velocity = 0
                self.vy = 0
                # update new position
                self.rect.y = self.y
                    
    def update(self):
        self.get_keys()
        # # set sprite rectangle position
        # self.rect.x = self.x * TILESIZE
        # self.rect.y = self.y * TILESIZE
        # this will make movement independant of frame rate
        self.x += self.vx * self.game.dt # get dt from game object
        self.y += self.vy * self.game.dt # get dt from game object
        # self.rect.topleft = (self.x, self.y)
        
        self.rect.x = self.x
        self.collide_with_walls('x')
        
        self.rect.y = self.y
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