# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 23:13:08 2020

@author: crtom
"""

import pygame as pg
from settings import *
from tilemap import collide_hit_rect

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
        
        self.hit_rect = PLAYER_HIT_RECT
        self.hit_rect.center = self.rect.center
        
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
            self.rot_speed = PLAYER_ROT_SPEED
        elif keys[pg.K_RIGHT] or keys[pg.K_d]: # IF ENABLES DIAG
            self.rot_speed = -PLAYER_ROT_SPEED
        if keys[pg.K_UP] or keys[pg.K_w]: # IF ENABLES DIAG
            self.vel = vec(PLAYER_SPEED, 0).rotate(-self.rot)
        # backwards move is slower
        if keys[pg.K_DOWN] or keys[pg.K_s]: # IF ENABLES DIAG
            self.vel = vec(-PLAYER_SPEED / 2, 0).rotate(-self.rot)
    
    def collide_with_walls(self, direction):
        # x collision check
        if direction == 'x':
            
            # modify this to use hit_rect instead
            #hits = pg.sprite.spritecollide(self, self.game.walls, False) # false= dont delete the wall
            hits = pg.sprite.spritecollide(self, 
                                           self.game.walls, 
                                           False,
                                           collide_hit_rect) # false= dont delete the wall
            
            if hits:
                # sprite was moving to the right
                # we need to put the sprite to the left edge of the wall
                if self.vel.x > 0:
                    #because we use rectangle centre / 2
                    self.pos.x = hits[0].rect.left - self.hit_rect.width / 2
                # sprite was moving to the left
                # we need to put the sprite to the right edge of the wall
                if self.vel.x < 0:
                    self.pos.x = hits[0].rect.right + self.hit_rect.width / 2 #- self.rect.width    
                
                # we run into the wall, x velocity = 0
                self.vel.x = 0
                # update new position of hit_rect
                self.hit_rect.centerx = self.pos.x

        if direction == 'y':
            #hits = pg.sprite.spritecollide(self, self.game.walls, False) # false= dont delete the wall
            hits = pg.sprite.spritecollide(self, 
                                           self.game.walls,
                                           False,
                                           collide_hit_rect) # false= dont delete the wall
            
            if hits:
                # sprite was moving down
                # we need to put the sprite to the top of the wall
                if self.vel.y > 0: 
                    self.pos.y = hits[0].rect.top - self.hit_rect.height / 2
                # sprite was moving to the top
                # we need to put the sprite to the bottom edge of the wall
                if self.vel.y < 0:
                    self.pos.y = hits[0].rect.bottom + self.hit_rect.height / 2 #- self.rect.width    
                
                # we run into the wall, x velocity = 0
                self.vel.y = 0
                # update new position of hit_rect
                self.hit_rect.centery = self.pos.y
                    
    def update(self):
        # 1.) read keyboard
        self.get_keys()
        # 2.) calculate rotation
        self.rot = (self.rot + self.rot_speed*self.game.dt) % 360
        # 3.) Update player sprite image with rotation
        self.image = pg.transform.rotate(self.game.player_img, self.rot)
        
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        # 4.) calculate position
        # this will make movement independant of frame rate
        self.pos += self.vel * self.game.dt # get dt from game object
        
        # 5.) check if collision with walls
        # if collision, than dont reverse to old position aka dont move
        self.hit_rect.centerx = self.pos.x
        self.collide_with_walls('x')
        
        self.hit_rect.centery = self.pos.y
        self.collide_with_walls('y')
        
        # 6.)when we update movement, be set equal 
        # sprite image rectangle and hit rectangle
        self.rect.center = self.hit_rect.center


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