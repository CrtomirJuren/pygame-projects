"""
Basic Movement and Key Presses
video: https://www.youtube.com/watch?v=i6xMBig-pP4&list=PLzMcBGfZo4-lp3jAExUCewBfMx3UZFkh5

1. create a rectangle
2. move it by key pressed
"""

import pygame
from pygame.locals import *
from sys import exit
from gameobjects.vector2 import Vector2

def draw_vector(screen, startpoint, vector, color, width, DEBUG = False):
    """
             E
            ***
           *****
          L**M**R
             *
             *
             *
             *
         ----S-----
             *
             *
             O
    
    E - vector endpoint  
    M - arrow midpoint  
    L - arrow left point  
    R - arrow right point  
    """
    #------------CALCULATIONS---------------
    #DEBUG = False
    # create points
    E = (0, 0) 
    L = (0, 0)
    M = (0, 0)
    R = (0, 0)

    # copy vector to new
    v = Vector2(int(vector.x), int(vector.y))
    
    # 1) set S - starrpoint
    S = (startpoint[0], startpoint[1])
    
    # 2) set E - endpoint
    E = (v.x + S[0], v.y + S[1])
    
    # 3) Find vector SM
    v_SM = Vector2(v.x, v.y)
    v_SM.normalize()
    v_SM *= 2*width # v_SM *= 10
    v_SM = v - v_SM
    
    M = (S[0]+v_SM.x, S[1]+v_SM.y) 
    
    # 3) Find perpendicular vector
    v_perp = Vector2(-v.y, v.x)
    v_perp.normalize()
    v_perp *= width # v_perp *= 5
    
    # 4) Find arrow head points
    L = (M[0] - v_perp.x, M[1] - v_perp.y)
    R = (M[0] + v_perp.x, M[1] + v_perp.y)
    
    #------------DRAWINGS---------------
    # pixels must be integers
    E = (int(E[0]),int(E[1]))
    M = (int(M[0]),int(M[1]))
    L = (int(L[0]),int(L[1]))
    R = (int(R[0]),int(R[1]))
    
    # draw main vector line
    pygame.draw.line(screen, color, S, M, width)
    
    # draw points for debugging purpose
    # points = S, E, L, M, R
    
    # draw arrow head poligone
    # if very short, dont draw arrow
    #length = sqrt(v.x
    pygame.draw.polygon(screen, color, (L, R, E))
    


WIDTH, HEIGHT = 1000, 800
FPS = 60

WHITE   = (255, 255, 255)
BLACK   = (0, 0, 0)
RED     = (255,0,0)
LIME    = (0,255,0)
BLUE    = (0,0,255)
YELLOW  = (255,255,0)

pygame.init()
pygame.mixer.init()

#### Create a canvas on which to display everything ####
screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
#set windows title
pygame.display.set_caption("8 way movement vector")
# set clock
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((64, 64))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        # delta time, game loop time
        #self.dt = 0
        
        # position vector
        self.position =  Vector2(100.0, 100.0)
        # direction vector
        self.direction = Vector2(0, 0)  
        # movement speed
        self.speed = 300.        
      

    #def set_time_passed_sec(self, dt):
    #    self.dt_sec = dt / 1000.0
        
    def update(self, dt):
        dt_sec = dt / 1000.0
        
        self.direction.x, self.direction.y = (0, 0)
        
        keystate = pygame.key.get_pressed()
    
        if keystate[pygame.K_UP]:
            self.direction += Vector2(0, -1)
        
        if keystate[pygame.K_DOWN]:
            self.direction += Vector2(0,  1)
        
        if keystate[pygame.K_LEFT]:
            self.direction += Vector2(-1, 0)
        
        if keystate[pygame.K_RIGHT]:
            self.direction += Vector2(1,  0)
        
        # direction vector is a unit vector, normalize it
        # diagonals are 0.707
        self.direction.normalize()
    
        self.position += self.direction * self.speed * dt_sec
        
        # set sprite rectangle position
        self.rect.x = self.position.x
        self.rect.y = self.position.y



all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
    
#main game loop
running = True
while running:
    dt = clock.tick(FPS)
    dt_sec = dt / 1000.0
    
    # pygame.time.delay(100) #this will be a clock for the game
    for event in pygame.event.get(): #check for all events that are happening
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    # update
    #player.set_time_passed_sec(dt)
    all_sprites.update(dt)
      
    screen.fill(BLACK)
    all_sprites.draw(screen)

    v_dir = Vector2(player.direction.x, player.direction.y)
    v_dir *= 100
    draw_vector(screen, (player.rect.center[0], player.rect.center[1]), v_dir, BLUE, 4)
        
    pygame.display.update()

# exit pygame
pygame.quit()
exit()
