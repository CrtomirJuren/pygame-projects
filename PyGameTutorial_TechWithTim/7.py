"""
6.py
website: https://techwithtim.net/tutorials/game-development-with-python/pygame-tutorial/pygame-animation/
video: https://www.youtube.com/watch?v=2-DNswzCkqk&list=PLzMcBGfZo4-lp3jAExUCewBfMx3UZFkh5&index=2

Creating HIT BOXES for collision programming
"""
import pygame
pygame.init()
#-----------------------------------------------------------
win = pygame.display.set_mode((500,480))
pygame.display.set_caption("First Game")
clock = pygame.time.Clock()

#-----------------------------------------------------------
# backgraound
bg = pygame.image.load('graphics/bg.jpg')
# character
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

standing = pygame.image.load('graphics/standing.png')


#--------------------------------------------------------------------
class enemy(object):
    #Enemy
    walkRightEnemy = [
    pygame.image.load('graphics/R1E.png'),
    pygame.image.load('graphics/R2E.png'),
    pygame.image.load('graphics/R3E.png'),
    pygame.image.load('graphics/R4E.png'),
    pygame.image.load('graphics/R5E.png'),
    pygame.image.load('graphics/R6E.png'),
    pygame.image.load('graphics/R7E.png'),
    pygame.image.load('graphics/R8E.png'),
    pygame.image.load('graphics/R9E.png')]

    walkLeftEnemy = [
    pygame.image.load('graphics/L1E.png'),
    pygame.image.load('graphics/L2E.png'),
    pygame.image.load('graphics/L3E.png'),
    pygame.image.load('graphics/L4E.png'),
    pygame.image.load('graphics/L5E.png'),
    pygame.image.load('graphics/L6E.png'),
    pygame.image.load('graphics/L7E.png'),
    pygame.image.load('graphics/L8E.png'),
    pygame.image.load('graphics/L9E.png')]

    def __init__(self,x,y,width,height,end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.walkCount = 0
        self.vel = 5
        self.path= [self.x,self.end]
        self.hitbox = (self.x + 20, self.y, 28, 60) #rectangle

        #self.left = False
        #self.right = False
    def draw(self, win):
        self.move()

        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        #are we moving right or left
        if self.vel > 0:
            win.blit(self.walkRightEnemy[self.walkCount//3],(self.x,self.y))
            self.walkCount += 1
        if self.vel < 0:
            win.blit(self.walkLeftEnemy[self.walkCount//3],(self.x,self.y))
            self.walkCount += 1

        #update hitbox
        self.hitbox = (self.x + 20, self.y, 28, 60)
        #draw hitbox
        pygame.draw.rect(win,(255,0,0),self.hitbox,2)

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:    #character path limits
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    def hit(self):
        print("hit")
        pass

#--------------------------------------------------------------------
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
        self.hitbox = (self.x + 20, self.y, 28, 60) #rectangle

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

        #update hitbox
        self.hitbox = (self.x + 20, self.y, 28, 60)
        #draw hitbox
        pygame.draw.rect(win, (255,0,0), self.hitbox, 2)
#---------------------------------------------------------------------------
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

#------------------------------------------------------------------------
def redrawGameWindow():
    #draw background
    win.blit(bg, (0,0))
    #draw character
    man.draw(win)
    #draw enemy
    goblin.draw(win)
    #draw all bullets
    for bullet in bullets:
        bullet.draw(win)
    #update everything to display
    pygame.display.update()
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#mainloop
man = player(200, 410, 64,64)
goblin = enemy(100, 410, 61, 61, 450)
shootLoop = 0
bullets = [] #list for multiple projectiles objects
#------------------------------------------------------------------------
run = True
while run:
    clock.tick(27)
    #---------------------------------------------
    print(shootLoop)
    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 5:
        shootLoop = 0

    #----------------escape keys---------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #--------------------------------------------
    for bullet in bullets:

        #goblin.hitbox[x coor, y coor,width]
        #checking for collision with enemy hitbox rectangle
        # ARE WE IN THE MIDDLE OF HITBOX Y
        if bullet.y - bullet.radius < goblin.hitbox[1]+goblin.hitbox[3] and bullet.y+bullet.radius>goblin.hitbox[1]:
            # ARE WE IN THE MIDDLE OF HITBOX x
            if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0]+goblin.hitbox[2]:
                #if we are inside the goblin hitbox
                goblin.hit()
                #if goblin was hit, remove bullet from the screen-list
                bullets.pop(bullets.index(bullet))

        # check if bullet is on screen
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        #if bullet of screen, remove it from list of bullets
        else:
            bullets.pop(bullets.index(bullet)) #find bullet in the list, that is off the screen
    #---------------------------------------------------------------------------------
    keys = pygame.key.get_pressed()

    # check if we pressed fire bullet
    if keys[pygame.K_SPACE] and shootLoop == 0:
        #set direction of bullet
        if man.left:
            man.facing = -1
        else:
            man.facing = 1

        #set maximum number of bullets at one time on screen
        if len(bullets) < 5:
            #bullets start at the middle of the man
            bullets.append(projectile((man.x + man.width//2), round(man.y + man.height//2),6, (0,0,0),man.facing))

        shootLoop = 1

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
#-----------------------------------------------------------
pygame.quit()