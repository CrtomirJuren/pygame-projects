"""
website: https://techwithtim.net/tutorials/game-development-with-python/pygame-tutorial/pygame-animation/
Character Animation
video: https://www.youtube.com/watch?v=2-DNswzCkqk&list=PLzMcBGfZo4-lp3jAExUCewBfMx3UZFkh5&index=2

"""
import pygame
pygame.init()

win = pygame.display.set_mode((500,480))

pygame.display.set_caption("First Game")

walkRight = [
pygame.image.load('graphics/R1.png'),
pygame.image.load('graphics/R2.png'),
pygame.image.load('graphics/R3.png'),
pygame.image.load('graphics/R4.png'),
pygame.image.load('graphics/R5.png'),
pygame.image.load('graphics/R6.png'),
pygame.image.load('graphics/R7.png'),
pygame.image.load('graphics/R8.png'),
pygame.image.load('graphics/R9.png')]

walkLeft = [
pygame.image.load('graphics/L1.png'),
pygame.image.load('graphics/L2.png'),
pygame.image.load('graphics/L3.png'),
pygame.image.load('graphics/L4.png'),
pygame.image.load('graphics/L5.png'),
pygame.image.load('graphics/L6.png'),
pygame.image.load('graphics/L7.png'),
pygame.image.load('graphics/L8.png'),
pygame.image.load('graphics/L9.png')]

bg = pygame.image.load('graphics/bg.jpg')

standing = pygame.image.load('graphics/standing.png')
clock = pygame.time.Clock()


class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.standing = True

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        #is player standing still or moving
        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
        else:
            #win.blit(char, (self.x,self.y))
            if self.right:
                win.blit(walkRight[0], (self.x,self.y))
            if self.left:
                win.blit(walkLeft[0], (self.x,self.y))
            if self.standing == True:
                win.blit(standing, (self.x,self.y))

class projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing #1 = left, -1 = right
        self.vel = 8 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


def redrawGameWindow():
    #draw background
    win.blit(bg, (0,0))
    #draw character
    man.draw(win)
    #draw all bullets
    for bullet in bullets:
        bullet.draw(win)
    #update everything to display
    pygame.display.update()


#mainloop
man = player(200, 410, 64,64)
bullets = [] #lsit for multiple projectiles objects

run = True
while run:
    clock.tick(27)
    #----------------escape keys---------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #--------------------------------------------
    for bullet in bullets:
        # check if bullet is on screen
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        #if bullet of screen, remove it from list of bullets
        else:
            bullets.pop(bullets.index(bullet)) #find bullet in the list, that is off the screen

    keys = pygame.key.get_pressed()

    # check if we pressed fire bullet
    if keys[pygame.K_SPACE]:
        #set maximum number of bullets at one time on screen
        if len(bullets) < 5:
            #set direction of bullet
            if man.left:
                man.facing = -1
            else:
                man.facing = 1
            #bullets start at the middle of the man
            bullets.append(projectile((man.x + man.width//2), round(man.y + man.height//2),6, (0,0,0),man.facing))

    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x < 500 - man.width - man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
        man.standing = False
    else:
        man.standing = True
        #man.right = False
        #man.left = False
        man.walkCount = 0

    if not(man.isJump):
        if keys[pygame.K_UP]:
            man.isJump = True
            #man.right = False
            #man.left = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10

    redrawGameWindow()

pygame.quit()